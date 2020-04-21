# -*-coding：utf-8-*-


from aip import AipOcr

config = {
    'appId': '18551409',
    'apiKey': 'uQ8YmvGmfcGhGy8UaRHkvd0W',
    'secretKey': 'iYYCbEcFYsgnyLNGaVaKso4eZ8MI3r7Z',

}
client = AipOcr(**config)


# 获取图像内容
def get_file_content(file):
    with open(file, 'rb') as f:
        return f.read()


# 把图片里的文字识别出来
def img_to_str(imag_path):
    image = get_file_content(imag_path)
    result = client.handwriting(image)
    # print(result)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])


# res = img_to_str(r'D:\20200421124055.png')
# print(res)
