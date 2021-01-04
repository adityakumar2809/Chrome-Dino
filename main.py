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
    background_dimensions
):
    pixel_object = image.load()
    for i in range(ground_crop_dimensions[0], ground_crop_dimensions[2]):
        for j in range(ground_crop_dimensions[1], ground_crop_dimensions[3]):
            pixel_object[i, j] = (255, 0, 0)

    for i in range(sky_crop_dimensions[0], sky_crop_dimensions[2]):
        for j in range(sky_crop_dimensions[1], sky_crop_dimensions[3]):
            pixel_object[i, j] = (0, 0, 255)

    for i in range(
        background_dimensions[0],
        background_dimensions[2]
    ):
        for j in range(
            background_dimensions[1],
            background_dimensions[3]
        ):
            pixel_object[i, j] = (0, 255, 0)
    image.show()


def isObstacleDetected(pixel_object, crop_dimensions, background_color):
    for i in range(crop_dimensions[2], crop_dimensions[0], -1):
        if pixel_object[i, crop_dimensions[1]] != background_color:
            return True
    return False


def hitKeyboard(key):
    pyautogui.press(key)


if __name__ == "__main__":
    debug = False
    ground_crop_dimensions = [250, 690, 350, 700]
    sky_crop_dimensions = [250, 620, 350, 630]
    background_dimensions = [200, 150, 210, 160]
    screen_width = 1920

    x_start = ground_crop_dimensions[0]
    x_end = ground_crop_dimensions[2]
    y_ground = (ground_crop_dimensions[1] + ground_crop_dimensions[3])//2
    y_sky = (sky_crop_dimensions[1] + sky_crop_dimensions[3])//2
    x_background = (background_dimensions[0] + background_dimensions[2])//2
    y_background = (background_dimensions[1] + background_dimensions[3])//2

    if debug:
        image = takeScreenshot()
        drawOnImage(
            image,
            ground_crop_dimensions,
            sky_crop_dimensions,
            background_dimensions
        )
    else:
        print('Dino game commences in 3 seconds...')
        time.sleep(3)
        hitKeyboard('up')

        iterations = 0

        while True:
            if(iterations % 100 == 0):
                if x_end < screen_width-3:
                    x_end += 6
            iterations += 1
            image = ImageGrab.grab().convert('L')
            pixel_object = image.load()
            background_color = pixel_object[x_background, y_background]

            for i in reversed(range(x_start, x_end)):
                if pixel_object[i, y_ground] != background_color or pixel_object[i, y_sky] != background_color:
                    pyautogui.press('up')
                    time.sleep(0.08)
                    pyautogui.press('down')
                    break

