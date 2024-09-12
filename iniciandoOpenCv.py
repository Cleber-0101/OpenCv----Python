import cv2

video = cv2.VideoCapture('runners.mp4')

while True:
    check, img = video.read()
    print(img.shape)
    cv2.imshow('Video', img)
    cv2.waitKey(0)