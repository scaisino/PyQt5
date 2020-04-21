# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Request
import json


def convert(s):
    if s is str and s.isdigit:
        return int(s.resplace(','))
    else:
        return 0


class XpcSpider(scrapy.Spider):
    name = 'xpc'
    allowed_domains = ['xinpianchang.com', 'openapi-vtom.vmovier.com']
    start_urls = ['https://www.xinpianchang.com/channel/index/sort-like?from=tabArticle']

    # 獲取每個視頻的鏈接
    def parse(self, response):
        pid_list = response.xpath(
            '//ul[@class="video-list"]/li[@class="enter-filmplay"]/@data-articleid').extract()  # pid列表

        cookies = {"Authorization": "01D3EF58AA36A73BCAA36A438BAA36A9459AA36AFD0C8371FE04"}

        for pid in pid_list:
            url = 'https://www.xinpianchang.com/a%s?from=ArticleList' % pid
            request = response.follow(url, self.parse_post)
            request.meta['pid'] = pid
            yield request
            '''
            pages=response.xpath('//div[@class="page-wrap"]/div[@class="page"]/a/@href').extract()
            
            for page in pages:
                yield response.follow(page,self.parse,cookies=cookies)
'''

    # 解析單個視頻信息
    def parse_post(self, response):
        pid = response.meta['pid']
        post = {
            "pid": pid
        }
        cotegray = response.xpath('//span[contains(@class,"cate")]/a/text()').extract()
        post['cotegray'] = '|'.join([cote.strip() for cote in cotegray])
        post['title'] = response.xpath('//div[@class="title-wrap"]/h3/text()').extract()
        post['play_counts'] = response.xpath('//i[@class="fs_12 fw_300 c_b_6 v-center play-counts"]/text()').extract()
        post['like_counts'] = response.xpath(
            '//span[@class="v-center like-counts fs_12 c_w_f fw_300"]/text()').extract()
        lable = response.xpath('//div[@class="fs_12 fw_300 c_b_3 tag-wrapper"]//text()').extract()
        post['lable'] = '|'.join([lab.strip() for lab in lable])

        # 視頻鏈接
        vid, = re.findall('vid: "(.*?)"', response.text)
        video_url = 'https://openapi-vtom.vmovier.com/v3/video/%s?expand=resource&usage=xpc_web' % vid
        request = Request(video_url, self.parse_video)
        request.meta['post'] = post
        yield request

        # 評論鏈接
        comment_url = "https://app.xinpianchang.com/comments?resource_id=%s&type=article&page=1&per_page=24" % pid
        request = Request(comment_url, self.parse_comment)
        yield request

        # 創作人信息
        cid_list = response.xpath('//ul[@class="creator-list"]/li/a/@data-userid').extract()
        creator_url = "https://www.xinpianchang.com/u%s?from=articleList"

        # 中间关系信息表
        for cid in cid_list:
            request = response.follow(creator_url % cid, self.parse_composer)
            request.meta['cid'] = cid
            yield request
            cr = {}
            cr['pid'] = pid
            cr['cid'] = cid
            cr['roles'] = response.xpath(
                '//ul[@class="creator-list"]/li/a[@data-userid=$var]/following-sibling::div['
                '1]/a/following-sibling::span/text()',
                var=cid).extract()
            yield cr

    # 作品信息表
    def parse_video(self, response):
        post = response.meta['post']

        result = json.loads(response.text)
        post['video'] = result['data']['resource']['default']['https_url']
        post['duration'] = result['data']['resource']['default']['duration']
        yield post

    # 评论信息表
    def parse_comment(self, response):
        comment = {}
        result = json.loads(response.text)
        list = result['data']['list']
        for li in list:
            # 評論人信息：名字、頭像、id、當前作品pid、評論、評論被點贊
            comment['uname'] = li['userInfo']['username']
            comment['avatar'] = li['userInfo']['avatar']
            comment['cid'] = li['userInfo']['id']
            comment['pid'] = li['resource_id']
            comment['contentlove'] = li['count_approve']
            comment['content'] = li['content']
        yield comment

    # 工作人员信息
    def parse_composer(self, response):
        composer = {}
        composer['banner'] = response.xpath('//div[@class="banner-wrap"]/@style').extract()
        composer['name'] = response.xpath('//div[@class="creator-info"]/p[@class="creator-name fs_26 fw_600 '
                                          'c_b_26"]/text()').extract()
        composer['like_counts'] = convert(response.xpath('//div[@class="creator-info"]/p[@class="creator-det'
                                                         'ail fs_14 fw_300 c_b_9"]/span[@class="like-wrap"]/span[2]/text()').extract())
        composer['fans_counts'] = response.xpath('//span[@class="fans-wrap"]/span[2]/text()').extract()
        composer['follow_counts'] = response.xpath('  //div[@class="creator-info"]/p[@class="creator-detail fs_14 fw'
                                                   '_300 c_b_9"]/span[@class="follow-wrap"]/span[2]/text()').extract()
        composer['location'] = response.xpath(
            '//span[@class="icon-location v-center"]/following-sibling::span[1]/text()').extract()
        composer['carerr'] = response.xpath('  //div[@class="creator-info"]/p[@class="creator-detail fs_14 fw_300 c_b_9'
                                            '"]/span[@class="icon-career v-center"]/following-sibling::span[1]/text()').extract()
        yield composer
