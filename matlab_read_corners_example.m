% Read ChArUco corner coordinates and IDs from .mat file

% Initialize parameters
MAX_CORNERS_IN_CHECKERBOARD = 88;
WRITTEN_IMAGES = 2;
CORNERS_FILENAME = 'corners.mat';
IDS_FILENAME = 'ids.mat';

% Read .mat files
[corners, ids] = read_corners_from_mat(MAX_CORNERS_IN_CHECKERBOARD, ...
    WRITTEN_IMAGES, CORNERS_FILENAME, IDS_FILENAME);
