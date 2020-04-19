from prompt_toolkit import document
from selenium import webdriver
import time
import re
def search_product():
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(kw)
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
# 强行阻止程序
    time.sleep(10)
    token = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token = int(re.compile('(\d+)').search(token).group(1))
    return token
def drop_down():
    for x in range(1,11,2):
        time.sleep(0.5)
        # 代表要滚动的位置
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)
def get_product():
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]').text
        price = div.find_element_by_xpath('.//a[@class="J_ClickStat"]').get_attribute('trace-price') + '元'
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        image = div.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('src')
        name = div.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
        position = div.find_element_by_xpath('.//div[@class="row row-3 g-clearfix"]/div[@class="location"]').text
        product = {'标题':info,'价格':price,'订单量':deal,'图片':image,'名字':name,}
        print(product)

def next_page():
    token = search_product()
    drop_down()
    get_product()
    num = 1
    while num != token:
        driver.get('https://s.taobao.com/search?q={}&s={}'.format(kw,44*num))
        # 隐士等待 智能等待时间为10s
        driver.implicitly_wait(10)
        num += 1
        drop_down()
        get_product()


if __name__ =='__main__':
    kw = input('请输入你要查询的商品：')
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com/')
    next_page()

