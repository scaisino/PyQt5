# -*-coding：utf-8-*-
from aip import AipOcr

config = {
    'appId': '19497493',
    'apiKey': 'VIFTg9DCwihn6LLW47M8vFpN',
    'secretKey': 'li81u532GNulkIbXUgWugL8dgH8PtCwL',

}
client = AipOcr(**config)


# 获取图像内容
def get_file_content(file):
    with open(file, 'rb') as f:
        return f.read()
# 把图片利的文字识别出来
def img_to_str(imag_path):
    image = get_file_content(imag_path)
    result = client.handwriting(image)
    print(result)
img_to_str(r'C:\Users\Administrator\Desktop\微信图片_20200420213822.jpg')