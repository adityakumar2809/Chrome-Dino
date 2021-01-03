import time

import pyautogui
from PIL import Image, ImageGrab


def takeScreenshot():
    image = ImageGrab.grab()
    image.show()


if __name__ == "__main__":
    takeScreenshot()