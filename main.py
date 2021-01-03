import time

import pyautogui
from PIL import Image, ImageGrab


def takeScreenshot():
    image = ImageGrab.grab()
    image.show()


def hitKeyboard(key):
    pyautogui.keyDown(key)


if __name__ == "__main__":
    takeScreenshot()