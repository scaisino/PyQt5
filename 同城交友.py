import os
import requests
import jsonpath
from urllib.request import urlretrieve
from 人像识别 import face_check
if not os.path.exists('./pic') :
    os.mkdir('./pic')
for i in range(1,5):

    url = f'http://www.7799520.com/api/user/pc/list/search?startage=21&endage=30&gender=2&cityid=180&startheight=151' \
          f'&endheight=160&marry=1&salary=2&page={i} '
    req = requests.get(url).json()
    print(req)
    avatars = jsonpath.jsonpath(req,'$..avatar')
    names = jsonpath.jsonpath(req,'$..username')
    print(avatars,names)
    for avatar,name in zip(avatars,names):
        print(avatar,name)
        #下载图片到pic文件夹
        urlretrieve(avatar,'./pic' + '/' + name + '.png')
path = r'D:\Envs\PyQt5\pic'
images = os.listdir(path)
print(images)
# 获取颜值分
yz = []
yz_dict = {}
for image in images:
    score = face_check(path + '/' + image)
    name = image[0:-4]
    yz.append(score)
    yz_dict[score] = name
yz.sort(reverse=True)
for a,b in enumerate(yz):
    print('小姐姐的名字是：{}=====他是第{}名=====他的颜值分是{}'.format(yz_dict[b],a+1,b))

