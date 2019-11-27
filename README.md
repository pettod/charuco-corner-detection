# ChArUco Corner Detection with OpenCV

## 1 Introduction

[Thesis](http://urn.fi/URN:NBN:fi:tty-201905101555)

Python OpenCV corner detection to detect [ChArUco](https://docs.opencv.org/3.2.0/df/d4a/tutorial_charuco_detection.html) markers and corners. The code finds chessboard corner coordinates and uses markers (QR-codes) to find IDs for the found corners. This project has also support for calling the corner detection through Matlab. Scripts provide real-time and still image visualization, and corner detection rate for set of images.

These scripts have been done in purpose of camera calibration so the goal was to find and identify corner coordinates. Expected outputs from the scripts are corner coordinates (x,y) in pixels and their corresponding IDs (from 0 to N-1).

<img src="document_images/detected_charuco_markers.gif"
     alt="ChArUco detected markers and corners"
     width="75%"
     style="display: block; margin-left: auto; margin-right: auto;" />

<img src="document_images/detected_charuco_corners.jpg"
     alt="ChArUco detected corners"
     width="75%"
     style="display: block; margin-left: auto; margin-right: auto;" />

## 2 Installation

1. Install Python 3.6. During the development, Python version 3.6.1 was used.

2. Clone the repository and install Python dependencies

```bash
git clone https://github.com/pettod/charuco-corner-detection.git
cd charuco-corner-detection
pip install -r requirements.txt
```

## 3 Usage

### 3.1 Setting Correct ChArUco Parameters

Python scripts have a few certain constant values that define the parameters needed to detect the markers in the given ChArUco calibration board. Check details to define the parameters for your ChArUco board:

[Setting ChArUco parameters](documentation/setting_parameters.md)

### 3.2 Running the Code

Descriptions for the scripts in the repository are described behind the following link:

[Descriptions of scripts](documentation/description_of_scripts.md)

Run the Python scripts with example images:

```bash
python draw_still_image_corners.py
python image_set_detection_rate.py
python real_time_corner_detection.py
python write_corners_to_mat.py
```
