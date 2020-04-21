# -*-coding：utf-8-*-
# from CJY import Chaojiying_Client
import requests
import base64

session = requests.session()
yzm_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?'
data = {
    'login_site': 'E',
    'module': 'login',
    'rand': 'sjrand',
}
req = session.get(yzm_url, params=data)
with open('yzm.png', 'wb') as f:
    f.write(req.content)
point_map = {
    '1': '40,45',
    '2': '116,53',
    '3': '185,52',
    '4': '257,50',
    '5': '40,121',
    '6': '116,133',
    '7': '185,132',
    '8': '257,130'
}


def get_point(index):
    indexs = index.split(',')
    temp = []
    for index in indexs:
        temp.append(point_map[index])
    return ','.join(temp)


code = get_point(input('请输入验证码'))
data = {
    'answer': code,
    'rand': 'sjrand',
    'login_site': 'E',
}
cheak_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check?'
req = session.get(cheak_url, params=data)
print(req.text)
