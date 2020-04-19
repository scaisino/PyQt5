# -*-coding：utf-8-*-
import urllib.parse
import json
import requests
import jsonpath

# https://www.duitang.com/search/?kw=%E5%B0%8F%E5%A7%90%E5%A7%90&type=feed
# url
url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'
kw = '小姐姐'
urllib.parse.quote(kw)
num = 1
for index in range(0, 73, 24):
    url = url.format(kw, index)
    # 模拟浏览器请求资源
    response = requests.get(url)
    resp = response.text
    # 解析网页
    # 转换类型
    html = json.loads(resp)
    photos = jsonpath.jsonpath(html, '$..path')
    # print(photos)
    # 保存数据

    for i in photos:
        #
        a = requests.get(i)
        with open(r'.\pic\{}.jpg'.format(num), 'wb') as fp:
            fp.write(a.content)
            num += 1
