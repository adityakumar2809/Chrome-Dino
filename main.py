import time

import pyautogui
from PIL import Image, ImageGrab


def takeScreenshot():
    image = ImageGrab.grab()
    return image


def drawOnImage(image, ground_crop_dimensions, sky_crop_dimensions):
    pixel_object = image.load()
    for i in range(ground_crop_dimensions[0], ground_crop_dimensions[2]):
        for j in range(ground_crop_dimensions[1], ground_crop_dimensions[3]):
            if (i - ground_crop_dimensions[0] < 10) or \
                (ground_crop_dimensions[2] - i < 10) or \
                (j - ground_crop_dimensions[1] < 10) or \
                    (ground_crop_dimensions[3] - j < 10):

                pixel_object[i, j] = (255, 0, 0)

    for i in range(sky_crop_dimensions[0], sky_crop_dimensions[2]):
        for j in range(sky_crop_dimensions[1], sky_crop_dimensions[3]):
            if (i - sky_crop_dimensions[0] < 10) or \
                (sky_crop_dimensions[2] - i < 10) or \
                (j - sky_crop_dimensions[1] < 10) or \
                    (sky_crop_dimensions[3] - j < 10):

                pixel_object[i, j] = (0, 0, 255)
    image.show()


def isObstacleDetected(image):
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
    ground_crop_dimensions = (250, 650, 375, 700)
    sky_crop_dimensions = (250, 595, 375, 645)
    if debug:
        image = takeScreenshot()
        drawOnImage(image, ground_crop_dimensions, sky_crop_dimensions)
    else:
        print('Dino game commences in 3 seconds...')
        time.sleep(3)
        hitKeyboard('up')
        while True:
            image = ImageGrab.grab(bbox=ground_crop_dimensions).convert('L')
            if isObstacleDetected(image):
                hitKeyboard('up')
                continue
            image = ImageGrab.grab(bbox=sky_crop_dimensions).convert('L')
            if isObstacleDetected(image):
                hitKeyboard('down')
