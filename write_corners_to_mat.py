"""
Write Charuco checkerboard's detected corners and IDs to files. Give arguments
of locations from where the images are read. Before running, check the constant
parameters in the beginning of this code and change them to fit to the
Charuco checkerboard used in the images.

Example:
--------
$ python write_corners_to_mat.py path/to/images/*.jpg another/path/*.jpg
"""

# Libraries
import numpy as np
from glob import glob
import scipy.io
import sys
from get_charuco_corners import getCharucoCorners, \
                                drawDetectedCornersCharuco_own

# Project files
from utils import getImagesFromArguments


CORNERS_COORS_FNAME = "coords.mat"
CORNERS_IDS_FNAME = "ids.mat"
CORNERS_X = 11
CORNERS_Y = 8
MARKER_DICT = 5
SQUARE_LENGTH = 60
MARKER_LENGTH = 47
NUMBER_OF_CAMERAS = 20


def writeToFile(corners_coords, corners_ids):
    scipy.io.savemat(CORNERS_COORS_FNAME, mdict=corners_coords)
    scipy.io.savemat(CORNERS_IDS_FNAME, mdict=corners_ids)
    print("Corners and IDs has been written to files:",
          CORNERS_COORS_FNAME, CORNERS_IDS_FNAME)


def main():
    detected_corners_images = 0
    image_names = glob("test_images/*.jpg")
    coords = {}
    ids = {}
    images_without_detected_corners = []

    # If argument was given, change image path
    if len(sys.argv) > 1:
        image_names = getImagesFromArguments(sys.argv[1:])

    for i in range(len(image_names)):
        # Detect corners
        charuco_corners, charuco_ids = getCharucoCorners(image_names[i],
                                                         CORNERS_X,
                                                         CORNERS_Y,
                                                         MARKER_DICT,
                                                         SQUARE_LENGTH,
                                                         MARKER_LENGTH)

        # Add corners to dictionary
        key = "pos_" + str(int(i / NUMBER_OF_CAMERAS)) \
              + "_cam_" + str(int(i % NUMBER_OF_CAMERAS))
        coords[key] = charuco_corners
        ids[key] = charuco_ids

        # Count the number of detected images
        # Save image names without detected corners
        if (charuco_ids.size > 0):
            detected_corners_images += 1
        else:
            parsed_name = image_names[i].split('/')[-1].split('.')[0]
            images_without_detected_corners.append(parsed_name)

        print("Image: {}/{}, Images of detected corners: {}"
              .format(i+1, len(image_names), detected_corners_images),
              end="\r")

    print("\nDetected corners in images: {}/{}"
          .format(detected_corners_images, len(image_names)))

    # Print image names without detected corners
    if (len(images_without_detected_corners)):
        print("Images without detected corners:")
        for i in range(len(images_without_detected_corners)):
            print("{}. {}".format(i+1, images_without_detected_corners[i]))

    writeToFile(coords, ids)

main()
