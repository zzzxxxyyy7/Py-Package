import cv2 as cv


def QuitCheck():
    while True:
        if ord('q') == cv.waitKey(0):
            break

