"""
Draw one detected corners in still image. Give an image name as an argument.
In the code, change the Charuco checkerboard's parameters if it is not correct.
In this code the checkerboard has 11x8 corners, 5x5 marker resolution, square
length is 60mm and marker length is 47mm.

If any corner was detected, then image is plotted.
Example:
$ python draw_corners_still_image.py path/to/the/image.bmp

Pressing 'q' will close the image.
"""

# Libraries
import cv2
import numpy as np
import sys
from get_charuco_corners import getCharucoCorners, \
                                drawDetectedCornersCharuco_own

# Project files
from utils import getImagesFromArguments


if __name__ == "__main__":

    file_name = "test_images/im1.jpg"

    # If argument was given
    if len(sys.argv) > 1:
        file_name = getImagesFromArguments(sys.argv[1:][0])

    frame = cv2.imread(file_name)
    charuco_corners, charuco_ids = getCharucoCorners(frame, 11, 8, 5,
                                                     60, 47)

    # Draw corners
    drawDetectedCornersCharuco_own(frame, charuco_corners,
                                   charuco_ids)
    print("Number of detected corners:", charuco_ids.size)

    # Draw image or quit
    cv2.imshow('Image', frame)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
