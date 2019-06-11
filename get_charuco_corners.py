import cv2
import numpy as np


def getCharucoCorners(image, corners_x, corners_y, marker_dict,
                      square_length, marker_length):
    """
    Finds visible corners in Charuco checkerboard. Detects the markers
    (QR codes) in the board and based on found marker IDs it will find the
    chessboard corners between crossing markers.

    Parameters
    ----------
    image : numpy.array, str
        Two dimensional image matrix or image path (str). Image can be
        grayscale image or RGB image including 3 layers. Allowed shapes are
        (x, y, 1) or (x, y, 3) or "path/to/the/image.jpg".
    corners_x : int
        The number of checkerboard corners in x direction. The x and y corners
        must be given in correct order, in most cases corners_x <= corners_y.
    corners_y : int
        The number of checkerboard corners in y direction.
    marker_dict : int
        The number of bits (resolution) and the number of markers contained
        represented in integer value. The macros for integers can be found from
        OpenCV's documentation. Here are some common examples of the
        dictionaries:
            DICT_[number_of_bits]_markers_contained	|   Given parameter
            cv2.aruco.DICT_5X5_50                   |   4
            cv2.aruco.DICT_5X5_100                  |   5
            cv2.aruco.DICT_5X5_250                  |   6
            cv2.aruco.DICT_6X6_50                   |   8
            cv2.aruco.DICT_6X6_250                  |   10
    square_length : int
        The side length of a square in Charuco checkerboard in millimeters.
    marker_length : int
        The side length of a marker in Charuco checkerboard in millimeters.

    Return
    ------
    Tuple of 2 numpy.array(s)
        Found checkerboard corners' coordinates and IDs. The tuple shape is
        (corners, ids). Corners includes x and y coordinates and ID represents
        the corner IDs in the same order as the coordinates are represented in
        the corners array.
    """

    # Define QR table
    dictionary = cv2.aruco.getPredefinedDictionary(marker_dict)

    # Define charuco board
    board_squares_x = corners_x + 1
    board_squares_y = corners_y + 1
    board = cv2.aruco.CharucoBoard_create(board_squares_x,
                                          board_squares_y,
                                          square_length/1000,
                                          marker_length/1000,
                                          dictionary)

    # Read image if only path is given
    if (type(image) == str):
        image = cv2.imread(image)

    # Detect QR codes (markers)
    (corners, ids, _) = cv2.aruco.detectMarkers(image, dictionary)
    charuco_corners = np.array([])
    charuco_ids = np.array([])

    # Any marker is detected
    if (ids is not None):
        # Read chessboard corners between markers
        (_, c_corners, c_ids) = cv2.aruco.interpolateCornersCharuco(corners,
                                                                    ids,
                                                                    image,
                                                                    board)
        # Any corner is detected
        if c_ids is not None:
            charuco_corners = c_corners[:, 0]
            charuco_ids = c_ids[:, 0]

    return charuco_corners, charuco_ids


def drawDetectedCornersCharuco_own(img, corners, ids):
    """
    Draw rectangles and IDs to the corners

    Parameters
    ----------
    img : numpy.array()
        Two dimensional image matrix. Image can be grayscale image or RGB image
        including 3 layers. Allowed shapes are (x, y, 1) or (x, y, 3).
    corners : numpy.array()
        Checkerboard corners.
    ids : numpy.array()
        Corners' IDs.
    """

    rect_size = 5
    id_font = cv2.FONT_HERSHEY_SIMPLEX
    id_scale = 0.5
    id_color = (255, 255, 0)
    rect_thickness = 1

    # Draw rectangels and IDs
    for (corner, id) in zip(corners, ids):
        corner_x = int(corner[0])
        corner_y = int(corner[1])
        id_text = "Id: {}".format(str(id))
        id_coord = (corner_x + 2*rect_size, corner_y + 2*rect_size)
        cv2.rectangle(img, (corner_x - rect_size, corner_y - rect_size),
                      (corner_x + rect_size, corner_y + rect_size),
                      id_color, thickness=rect_thickness)
        cv2.putText(img, id_text, id_coord, id_font, id_scale, id_color)


def drawDetectedCornersCharuco(img, corners, ids):
    """
    Draw rectangles and IDs to the corners, wrapper

    Parameters
    ----------
    img : numpy.array()
        Two dimensional image matrix. Image can be grayscale image or RGB image
        including 3 layers. Allowed shapes are (x, y, 1) or (x, y, 3).
    corners : numpy.array()
        Checkerboard corners.
    ids : numpy.array()
        Corners' IDs.
    """

    id_color = (255, 255, 0)
    corners = corners.reshape((corners.shape[0], 1, corners.shape[1]))
    ids = ids.reshape((ids.size, 1))
    cv2.aruco.drawDetectedCornersCharuco(img, corners, ids, id_color)


if __name__ == "__main__":
    """
    Code example to show how the code works. It uses webcam to record video
    and the used charuco checkerboard is having 4x6 corners and 6x6 resolution
    of the markers (QR codes). Square length in the board is 35mm and marker
    length is 25mm.
    Pressing 'q' will stop the recording.
    """

    # Start capturing images from webcam
    cap = cv2.VideoCapture(0)
    while True:

        # Read one frame
        _, frame = cap.read()
        charuco_corners, charuco_ids = getCharucoCorners(frame, 4, 6, 8,
                                                         35, 25)

        # If any corner is detected, draw corner
        if (charuco_ids.size > 0):
            drawDetectedCornersCharuco(frame, charuco_corners,
                                       charuco_ids)

        # Draw image or quit
        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release capturing and close window
    cap.release()
    cv2.destroyAllWindows()
