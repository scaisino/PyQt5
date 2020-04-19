# -*-coding：utf-8-*-
# 首先pip install baidu-aip
# SDK文档链接http://ai.baidu.com/docs#/Face-Python-SDK/top
import base64
from aip import AipFace

APP_ID = '19497493'
API_KEY = 'VIFTg9DCwihn6LLW47M8vFpN'
SECRET_KEY = 'li81u532GNulkIbXUgWugL8dgH8PtCwL'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face_check(img_data):
    """
    人脸识别demo
    :param img_data: 二进制的图片数据
    :return:
    """

    data = base64.b64encode(img_data)

    image = data.decode()

    imageType = "BASE64"

    """ 调用人脸检测 """
    client.detect(image, imageType)

    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "beauty,age,faceshape,expression,gender,glasses"
    options["max_face_num"] = 10

    """ 带参数调用人脸检测 """
    res = client.detect(image, imageType, options)
    return  res['result']['face_list'][0]['beauty']
    print(res)
    try:
        res_list = res['result']
    except Exception as e:
        res_list = None

    return res_list


if __name__ == "__main__":
    with open("./pic/夏雪12345678.png", "rb") as f:
        data = f.read()

    res = face_check(data)
    print(res)
