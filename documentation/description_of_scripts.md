# Descriptions of Scripts

**Note: You must set correct parameters depending on your ChArUco calibration board before running the scripts.**

## 4.2.1 Python

1. ```draw_still_image_corners.py```

Visualizes detected ChArUco corners. The resulting image should be similar with the still image above where squares are drawn to the corners with corner ID. Run the script as follows:

```bash
python draw_still_image_corners.py path/to/image.jpg
```

where the argument is path to the still image.

2. ```image_set_detection_rate.py```

Computing the detection rate for a set of images is informative, and helps to see fast how good images were taken during the capturing process. The command line interface is similar to the still image case. The path to the image set or multiple paths of the image sets can be given as arguments for the code. The call is as follows:

```bash
python image_set_detection_rate.py path/*.jpg another/path/*.jpg
```

It prints information of how many images had at least 1 detected corner and the percentage of detected corners compared to maximum number of corners (which is the number of images multiplied by the number of corners in the ChArUco calibration board). 

3. ```real_time_corner_detection.py```

Runs real-time ChArUco marker and corner detection. It helps during the capturing session to see in real-time how well the markers are detected with different distances and angles in relation to a camera. Run the code as follows:

```bash
python real_time_corner_detection.py
```

Note: 6X6 ChArUco board is provided in the ```test_images/charuco_marker_6x6.png``` file. The board can be printed to a paper and tested out.

4. ```write_corners_to_mat.py```

Writes ChArUco calibration board's corner coordinates and IDs to ```.mat``` file. Multiple file formats or paths can be given as arguments. Run the code as follows:

```bash
python write_corners_to_mat.py path/*.jpg another/path/*.jpg
```

Note: It was noticed that Matlab (version R2018b) does not support
the NumPy library in Python 3.7. In Matlab, the image coordinates are then read from the ```.mat``` file.

## 4.2.2 Matlab

1. ```matlab_read_corners_example.m```

Example file on how to read the ChArUco corner coordinates and IDs from the written ```.mat``` file. Needs to know the written corner coordinates and IDs file names, maximum number of corners in the ChArUco calibration board and the number of written images. Uses file ```read_corners_from_mat.m``` for reading.

2. ```matlab_charuco_example.m```

Example file on how to use the ChArUco corner detection API through Matlab. This is the file for Matlab users who want directly detect ChArUco calibration board's corners with corner IDs by using only Matlab. If ChArUco corner detection is needed in your project, you will have to copy files ```charuco.py``` and ```detect_charuco_corners.m``` to your project folder.