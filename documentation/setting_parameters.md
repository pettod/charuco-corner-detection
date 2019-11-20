# Setting Parameters in Calibration Board

The table below describes the used parameters that must be defined. The main parameters are the first 3 ones which determine the number of corners and a marker resolution in the ChArUco calibration board.

| Parameter      | Description   |
| -------------- | ------------- |
| CORNERS_X      | The number of checkerboard corners in x direction |
| CORNERS_Y      | The number of checkerboard corners in y direction |
| MARKER_DICT    | Marker dictionary, depends on the marker resolution and the maximum number of needed marker IDs |
| SQUARE_LENGTH  | The side length of a square in a checkerboard pattern in millimeters |
| MARKER_LENGTH  | The side length of a marker in a checkerboard pattern in millimeters |

Note: Parameters CORNERS_X and CORNERS_Y must be given in correct order meaning that if some weird values are found for corner coordinates, you will have to swap the values between these parameters. The weird values can be noticed by visualizing the corner coordinates. MARKER_DICT values can be found from OpenCV's documentation under [cv::aruco::PREDEFINED_DICTIONARY_NAME](https://docs.opencv.org/4.1.0/d9/d6a/group__aruco.html#gac84398a9ed9dd01306592dd616c2c975), but the common possible enumerators and their integer values are also covered in the table below.

| Enumerator            | Value     |
| --------------------- | --------- |
| DICT_4X4_50    	    | 0         |
| DICT_4X4_100   	    | 1         |
| DICT_4X4_250   	    | 2         |
| DICT_4X4_1000  	    | 3         |
| DICT_5X5_50    	    | 4         |
| DICT_5X5_100   	    | 5         |
| DICT_5X5_250   	    | 6         |
| DICT_5X5_1000  	    | 7         |
| DICT_6X6_50    	    | 8         |
| DICT_6X6_100   	    | 9         |
| DICT_6X6_250   	    | 10        |
| DICT_6X6_1000  	    | 11        |
| DICT_7X7_50    	    | 12        |
| DICT_7X7_100   	    | 13        |
| DICT_7X7_250   	    | 14        |
| DICT_7X7_1000         | 15        |

The name of an enumerator defines the marker resolution and the maximum number of used corners in the dictionary. The maximum number of corners in the dictionary must always be greater or equal than the number of corners in the ChArUco calibration board that is currently in use.
