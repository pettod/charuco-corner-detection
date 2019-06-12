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

1. Clone the repository

```
git clone https://github.com/pettod/charuco-corner-detection.git
```

2. Install Python 3.6 and its dependencies

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

Python scripts have a few certain constant values that define the parameters needed to detect the markers in the given ChArUco checkerboard. The table below describes the used parameters that you must define mainly depending on the number of markers and marker resolution in your ChArUco checkerboard.

| Parameter      | Description   |
| -------------- |:-------------:|
| CORNERS_X      | The number of checkerboard corners in x direction |
| CORNERS_Y      | The number of checkerboard corners in y direction |
| MARKER_DICT    | Marker dictionary, depends on the marker resolution and the maximum number of needed marker IDs |
| SQUARE_LENGTH  | The side length of a square in ChArUco checkerboard in millimeters |
| MARKER_LENGTH  | The side length of a marker in ChArUco checkerboard in millimeters |

Explanations for the scripts in the repository:

#### Python

1. ```draw_corners_still_image.py```

2. ```how_many_images_can_be_read.py```

3. ```real_time_corner_detection.py```

4. ```write_corners_to_mat.py```

#### Matlab

1. ```read_coordinates_from_mat.m```