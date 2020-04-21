# -*-coding：utf-8-*-
import os
from urllib.request import urlretrieve
from tkinter import *
import requests
from selenium import webdriver

# 功能模块
# url = 'https://music.163.com/#/search/m/?s={}&type=1'
# url2 = 'https://music.163.com/song/media/outer/url?id={}.mp3'

headers = {
    'Referer': 'https://music.163.com/', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                                                       'KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 '
}


# 下载歌曲
def song_load(item):
    song_id = item['song_id']
    song_name = item['song_name']
    song_url = 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
    # 创建文件夹
    os.makedirs('music', exist_ok=True)
    path = 'music\{}.mp3'.format(song_name)
    # 文本框
    text.insert(END, '歌曲：{},正在下载...'.format(song_name))
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()
    # 下载
    urlretrieve(song_url, path)
    # 文本框
    text.insert(END, '下载完毕：{},请试听...'.format(song_name))
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()


# 搜索歌曲名称
def get_music_name():
    name = entry.get()
    url = 'https://music.163.com/#/search/m/?id=1441018380&s={}&type=1'.format(name)
    # 隐藏浏览器
    option = webdriver.ChromeOptions()
    option.add_argument('-headless')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')
    # 获取歌曲id
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute("href")
    print(a_id)
    song_id = a_id.split('=')[-1]
    print(song_id)
    # 获取歌曲名称
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute("title")
    print(song_name)
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name

    driver.quit()  # 退出浏览器
    song_load(item)


# 创建界面
root = Tk()
# 创建窗口标题
root.title('网易云音乐下载器')
# 设置窗口尺寸
root.geometry('560x450')
# 标签控件
label = Label(root, text='请输入歌曲名称：', font=('华文行楷', 20))
# 标签定位
label.grid()
# 输入框
entry = Entry(root, font=('隶属', 20))
entry.grid(row=0, column=1)
# 列表框
text = Listbox(root, font=('楷书', 16), width=50, heigh=15)
text.grid(row=1, columnspan=2)
# 开始按钮
button = Button(root, text='开始下载', font=('隶属', 15), command=get_music_name)
button.grid(row=2, column=0, sticky=W)
# 退出按钮
button = Button(root, text='退出程序', font=('隶属', 15), command=root.quit)
button.grid(row=2, column=1, sticky=E)
# 显示界面
root.mainloop()
