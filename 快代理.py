# -*-coding：utf-8-*-
import requests
import parsel

proxies_list = []
for page in range(1,5):
    print('=============正在获取第{}数据============'.format(page))
    base_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(str(page))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/81.0.4044.113 Safari/537.36'}
    response = requests.get(base_url, headers=headers)
    # print(response.request.headers)
    data = response.text
    # print(data)
    # 转换数据类型
    html_data = parsel.Selector(data)
    # 数据解析
    parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

    # 循环遍历
    for tr in parse_list:
        dict_proxies = {}
        http_type = tr.xpath('./td[4]/text()').extract_first() # 协议类型
        ip_num = tr.xpath('./td[1]/text()').extract_first() # 协议类型
        ip_port = tr.xpath('./td[2]/text()').extract_first() # 协议类型
        # print(http_type,ip_num,ip_port)
        # 构建ip字典
        dict_proxies[http_type] = ip_num + ':' + ip_port
        # print(dict_proxies)
        proxies_list.append(dict_proxies)

print(proxies_list)
print('获取到的代理ip的数量：', len(proxies_list))



