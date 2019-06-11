import cv2
import numpy as np
import sys
import time


COLOR = 1	            # Color or gray image
DRAW_CORNERS = 1	    # Chessboard corners
DRAW_MARKERS = 1        # Charuco QR-codes
PRINT_MARKER_IDS = 1    # Print QR-codes' IDs

"""
cv2.aruco.DICT_5X5_50   4
cv2.aruco.DICT_5X5_100	5
cv2.aruco.DICT_5X5_250	6
cv2.aruco.DICT_6X6_50   8
cv2.aruco.DICT_6X6_250	10
"""
MARKER_DICT = 8
BOARD_CORNERS_SHAPE = (4, 6)    # Number of X, Y corners,
                                # must be in correct order
SQUARE_LENGHT = 0.035   # Chessboard square side in meters
MARKER_LENGTH = 0.025   # QR-code side in meters


def remove_printed_line():
    """
    Remove previous printed line
    """

    sys.stdout.write("\033[F")
    print("                              \
                                                ")
    sys.stdout.write("\033[F")


prev_ind = []
def print_marker_ids(indices):
    """
    Print marker IDs.
    """

    # Put indices into one list
    global prev_ind
    ind = []
    for i in indices:
        ind.append(i[0])
    ind.sort()

    # Avoid clear and print the same indices
    if prev_ind != ind:
        remove_printed_line()
        print("Marker Ids:", ind)


def drawDetectedCornersCharuco_own(img, corners, ids):
    """
    Draw rectangles and IDs to the corners
    """

    rect_size = 5
    id_font = cv2.FONT_HERSHEY_SIMPLEX
    id_scale = 0.5
    id_color = (255, 255, 0)
    rect_thickness = 1

    # Draw rectangels and IDs
    for (corner, id) in zip(corners, ids):
        corner_x = int(corner[0][0])
        corner_y = int(corner[0][1])
        id_text = "Id: {}".format(str(id[0]))
        id_coord = (corner_x + 2*rect_size, corner_y + 2*rect_size)
        cv2.rectangle(img, (corner_x - rect_size, corner_y - rect_size),
                      (corner_x + rect_size, corner_y + rect_size),
                      id_color, thickness=rect_thickness)
        cv2.putText(img, id_text, id_coord, id_font, id_scale, id_color)


def main():
    print()
    # Define QR indices up to 50 in dictionary
    dictionary = cv2.aruco.getPredefinedDictionary(MARKER_DICT)
    board_squares_x = BOARD_CORNERS_SHAPE[0] + 1
    board_squares_y = BOARD_CORNERS_SHAPE[1] + 1
    board = cv2.aruco.CharucoBoard_create(board_squares_x, board_squares_y,
                                          SQUARE_LENGHT, MARKER_LENGTH,
                                          dictionary)

    # Start capturing images
    cap = cv2.VideoCapture(0)

    charucoCorners = []
    charucoIds = []
    while True:

        # Read one frame
        ret, frame = cap.read()
        if not COLOR:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect QR codes (markers)
        res = cv2.aruco.detectMarkers(frame, dictionary)
        corners = res[0]
        ids = res[1]

        # Any marker is detected
        if (ids is not None):
            if PRINT_MARKER_IDS:
                print_marker_ids(ids)

            # Read chessboard corners between markers
            res2 = cv2.aruco.interpolateCornersCharuco(corners, ids, frame,
                                                       board)
            charucoCorners = res2[1]
            charucoIds = res2[2]

            # If any corner is detected, draw corner
            if (charucoIds is not None
                and DRAW_CORNERS):
                drawDetectedCornersCharuco_own(frame, charucoCorners,
                                               charucoIds)

            # Draw markers
            if DRAW_MARKERS:
                cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # Draw image or quit
        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release capturing and close window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
