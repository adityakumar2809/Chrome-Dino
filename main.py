import time

import pyautogui
from PIL import Image, ImageGrab


def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image


def drawOnImage(image):
    pixel_object = image.load()
    for i in range(215, 270):
        for j in range(500, 740):
            pixel_object[i, j] = 0
    image.show()


def hitKeyboard(key):
    pyautogui.keyDown(key)


if __name__ == "__main__":
    image = takeScreenshot()
    drawOnImage(image)