import time

import pyautogui
from PIL import Image, ImageGrab


def takeScreenshot():
    image = ImageGrab.grab()
    return image


def drawOnImage(
    image,
    ground_crop_dimensions,
    sky_crop_dimensions,
    background_detection_dimensions
):
    pixel_object = image.load()
    for i in range(ground_crop_dimensions[0], ground_crop_dimensions[2]):
        for j in range(ground_crop_dimensions[1], ground_crop_dimensions[3]):
            pixel_object[i, j] = (255, 0, 0)

    for i in range(sky_crop_dimensions[0], sky_crop_dimensions[2]):
        for j in range(sky_crop_dimensions[1], sky_crop_dimensions[3]):
            pixel_object[i, j] = (0, 0, 255)

    for i in range(
        background_detection_dimensions[0],
        background_detection_dimensions[2]
    ):
        for j in range(
            background_detection_dimensions[1],
            background_detection_dimensions[3]
        ):
            pixel_object[i, j] = (0, 255, 0)
    image.show()


def isObstacleDetected(pixel_object, crop_dimensions, background_color):
    for i in range(crop_dimensions[2], crop_dimensions[0], -1):
        for j in range(crop_dimensions[1], crop_dimensions[3]):
            if pixel_object[i, j] != background_color:
                return True
    return False


def hitKeyboard(key):
    pyautogui.press(key)


if __name__ == "__main__":
    debug = False
    ground_crop_dimensions = [250, 690, 600, 700]
    sky_crop_dimensions = [250, 620, 600, 630]
    background_detection_dimensions = [200, 150, 210, 160]
    if debug:
        image = takeScreenshot()
        drawOnImage(
            image,
            ground_crop_dimensions,
            sky_crop_dimensions,
            background_detection_dimensions
        )
    else:
        print('Dino game commences in 3 seconds...')
        time.sleep(3)
        hitKeyboard('up')
        while True:
            image = ImageGrab.grab().convert('L')
            pixel_object = image.load()
            background_color = pixel_object[205, 155]
            if isObstacleDetected(pixel_object, ground_crop_dimensions, background_color):
                hitKeyboard('up')
                continue
            if isObstacleDetected(pixel_object, sky_crop_dimensions, background_color):
                hitKeyboard('up')
