% Test script to show how to detect ChArUco corners and corner IDs

% Read image and set ChArUco checkerboard parameters
image = imread('test_images/im1.jpg');
cornersX = 11;
cornersY = 8;
markerResolution = 5;
squareLength = 60;
markerLength = 47;

% Detect corners with corner IDs
[imCorners, imIds] = detect_charuco_corners(image, cornersX, cornersY, ...
    markerResolution, squareLength, markerLength);
