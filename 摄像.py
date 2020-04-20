# -*-coding：utf-8-*-
import cv2


if __name__ == '__main__':
    cv2.namedWindow("camera", 1)

    capture = cv2.VideoCapture(0)
    with True:
        success, img = capture.read()
        cv2.imshow("camera", img)


