# OpenCV ChArUco Corner Detection

## Introduction
Python OpenCV corner detection to detect [ChArUco](https://docs.opencv.org/3.2.0/df/d4a/tutorial_charuco_detection.html) markers and corners. This project has also support for calling the corner detection through Matlab. This code detects markers (QR-codes) in the ChArUco board and interpolates the corners between 2 found markers. The corner IDs and coordinates are obtained in this project.

<img src="document_images/detected_charuco_corners.jpg"
     alt="ChArUco detected corners"
     style="float: center;" />

<img src="document_images/detected_charuco_markers.gif"
     alt="ChArUco detected markers and corners"
     style="float: center;" />

## Dependencies

In order to run python scripts through Matlab, you must have Python 3.6 installed. Otherwise, these should work with Python 3.7.

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

If you have version issues of the versions of libraries, these versions have been tested to work:
- Python 3.6.1
- numpy 1.16.4
- opencv 4.1.0
- scipy 1.3.0

## Usage
