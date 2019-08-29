"""
Code example to show how the code works. Charuco checkerboard has 11x8
corners, 5x5 marker resolution, square length is 60mm and marker length
is 47mm.
Takes command line arguments of paths from where to find images.

Example:
$ python how_many_images_can_be_read.py path/to/images/*.png another/path/*.jpg
"""

# Libraries
import cv2
import numpy as np
from glob import glob
import sys

# Project files
from charuco import getCharucoCorners, drawDetectedCornersCharuco_own
from utils import getImagesFromArguments


CORNERS_X = 11
CORNERS_Y = 8
MARKER_RESOLUTION = 5
SQUARE_LENGTH = 60
MARKER_LENGTH = 47


def main():
    detected_images = 0
    detected_corners = 0
    image_names = glob("test_data/*.jpg")

    # If argument was given
    if len(sys.argv) > 1:
        image_names = getImagesFromArguments(sys.argv[1:])

    # Loop images
    for i in range(len(image_names)):
        charuco_corners, charuco_ids = getCharucoCorners(image_names[i],
                                                         CORNERS_X,
                                                         CORNERS_Y,
                                                         MARKER_RESOLUTION,
                                                         SQUARE_LENGTH,
                                                         MARKER_LENGTH)

        # If any corner is detected, count it
        if (charuco_ids.size > 0):
            detected_images += 1
            detected_corners += charuco_corners.shape[0]

        print("Image: {}/{}, Detected: {}".format(i+1,
                                                  len(image_names),
                                                  detected_images),
              end="\r")

    print("\nSuccessfully detected corners in images: {}/{}"
          .format(detected_images, len(image_names)))
    print("Detection rate on average: {} %"
          .format(round(detected_corners / (CORNERS_X * CORNERS_Y *
                                            len(image_names)) * 100, 2)))


main()
