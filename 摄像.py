# -*-coding：utf-8-*-
import cv2
from 拍照识别 import img_to_str
if __name__ == '__main__':
    # 创建窗口 不能更改大小
    cv2.namedWindow("camera", 1)
    # 开启摄像头
    capture = cv2.VideoCapture(0)
    while True:
        success, img = capture.read()
        cv2.imshow("camera", img)
        # 按键处理
        key = cv2.waitKey(10)
        if key == 27:
            # esc键
            print('esc break')
            break

        if key == 32:
            # 空格键
            filename = 'frames.jpg'
            cv2.imwrite(filename, img)
            s = img_to_str(filename)
            print(s)

    # 释放掉摄像头
    capture.release()
    # 关闭窗口
    cv2.destroyWindow("camera")
