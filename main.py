import time

import pyautogui
from PIL import Image, ImageGrab


def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image


def drawOnImage(image):
    pixel_object = image.load()
    for i in range(215, 270):
        for j in range(500, 720):
            pixel_object[i, j] = 0
    image.show()

def isGroundObstacleDetected(image):
    pixel_object = image.load()
    for i in range(215, 270):
        for j in range(500, 720):
            if pixel_object[i, j] > 100:
                return True
    return False


def hitKeyboard(key):
    pyautogui.keyDown(key)


if __name__ == "__main__":
    print('Dino game commences in 3 seconds...')
    time.sleep(3)
    while True:
        image = takeScreenshot()
        # drawOnImage(image)
        # break
        if isGroundObstacleDetected(image):
            hitKeyboard('up')