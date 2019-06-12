# OpenCV ChArUco Corner Detection

## Introduction
Python OpenCV corner detection to detect [ChArUco](https://docs.opencv.org/3.2.0/df/d4a/tutorial_charuco_detection.html) markers and corners. This project has also support for calling the corner detection through Matlab. This code detects markers (QR-codes) in the ChArUco board and interpolates the corners between 2 found markers. Corner IDs and coordinates are obtained in this project. Scripts also provide real-time and still image visualization, and detection rate for set of images.

<img src="document_images/detected_charuco_corners.jpg"
     alt="ChArUco detected corners"
     width="75%"
     style="display: block; margin-left: auto; margin-right: auto;" />

<img src="document_images/detected_charuco_markers.gif"
     alt="ChArUco detected markers and corners"
     width="75%"
     style="display: block; margin-left: auto; margin-right: auto;" />

## Dependencies

These scripts have been tested in Manjaro 18.0.4 and in Windows 10. In order to run Python scripts through Matlab, you must have Python 3.6 installed. If Matlab support is not needed, the python scripts should work with Python 3.7 as well. All the scripts use OpenCV contrib modules which must be installed, see ```requirements.txt```.

## Installation

1. Install Python 3.6

2. Clone the repository

```
git clone https://github.com/pettod/charuco-corner-detection.git
```

3. Install Python dependencies

```
cd charuco-corner-detection
pip install -r requirements.txt
```

In case of having version issues with the libraries, at least these versions have been tested to work:
- Python 3.6.1
- numpy 1.16.4
- opencv 4.1.0
- scipy 1.3.0

## Usage

### Setting correct ChArUco parameters

Python scripts have a few certain constant values that define the parameters needed to detect the markers in the given ChArUco checkerboard. The table below describes the used parameters that must be defined. The main parameters are the first 3 ones which determine the number of corners and a marker resolution in the ChArUco checkerboard.

| Parameter      | Description   |
| -------------- | ------------- |
| CORNERS_X      | The number of checkerboard corners in x direction |
| CORNERS_Y      | The number of checkerboard corners in y direction |
| MARKER_DICT    | Marker dictionary, depends on the marker resolution and the maximum number of needed marker IDs |
| SQUARE_LENGTH  | The side length of a square in ChArUco checkerboard in millimeters |
| MARKER_LENGTH  | The side length of a marker in ChArUco checkerboard in millimeters |

Note: Parameters CORNERS_X and CORNERS_Y must be given in correct order meaning that if some weird values are found for corner coordinates, you will have to swap the values between these parameters. The weird values can be noticed by visualizing the corner coordinates. MARKER_DICT values can be found from OpenCV's documentation under [cv::aruco::PREDEFINED_DICTIONARY_NAME](https://docs.opencv.org/3.1.0/d9/d6a/group__aruco.html#gac84398a9ed9dd01306592dd616c2c975), but all the possible enumerators and their integer values are also covered in the table below.

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
| DICT_ARUCO_ORIGINAL   | 16        |

The name of an enumerator defines the marker resolution and the maximum number of used corners in the dictionary. The maximum number of corners in the dictionary must always be greater or equal than the number of corners in the ChArUco checkerboard that is currently in use.

### Running the code

Explanations for the scripts in the repository:

#### Python

1. ```draw_corners_still_image.py```

2. ```how_many_images_can_be_read.py```

3. ```real_time_corner_detection.py```

    - Note: 6X6 ChArUco board is provided in the ```test_images``` folder. The board can be printed and tested out.

4. ```write_corners_to_mat.py```

#### Matlab

1. ```read_coordinates_from_mat.m```