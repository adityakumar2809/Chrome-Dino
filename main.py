import time

import pyautogui
from PIL import Image, ImageGrab


def takeScreenshot():
    image = ImageGrab.grab()
    return image


def drawOnImage(image, crop_dimensions):
    pixel_object = image.load()
    for i in range(crop_dimensions[0], crop_dimensions[2]):
        for j in range(crop_dimensions[1], crop_dimensions[3]):
            pixel_object[i, j] = (255,0,0)
    image.show()

def isGroundObstacleDetected(image):
    pixel_object = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if pixel_object[i, j] > 100:
                return True
    return False


def hitKeyboard(key):
    pyautogui.press(key)


if __name__ == "__main__":
    debug = False
    crop_dimensions = (250, 650, 375, 700)
    if debug:
        image = takeScreenshot()
        drawOnImage(image, crop_dimensions)
    else:
        print('Dino game commences in 3 seconds...')
        time.sleep(3)
        hitKeyboard('up')
        while True:
            image = ImageGrab.grab(bbox=crop_dimensions).convert('L')
            if isGroundObstacleDetected(image):
                hitKeyboard('up')