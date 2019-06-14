% Detect ChArUco corners and corner IDs from image

function [imCorners, imIds] = detect_charuco_corners(...
    image, cornersX, cornersY, markerResolution, squareLength,...
    markerLength)

% Define maximum number of corners to the list
markerDict = 0;
if markerResolution == 4
    markerDict = 3;
elseif markerResolution == 5
    markerDict = 7;
elseif markerResolution == 6
    markerDict = 11;
elseif markerResolution == 7
    markerDict = 14;
end

% Detect corners with IDs
cornersAndIds = struct(py.charuco.matlabGetCharucoCorners(...
    py.numpy.array(image), cornersX, cornersY, markerDict, squareLength,...
    markerLength));
imCorners = numpyArray2matrix(cornersAndIds.corners);
imIds = numpyArray2vector(cornersAndIds.ids);

end


function matrix = numpyArray2matrix(numpyArray)

% Convert Python numpy.ndarray to Matlab matrix
arrayShape = double(py.array.array('d',numpyArray.shape));
vector = double(py.array.array('d',py.numpy.nditer(numpyArray)));
matrix = reshape(vector,fliplr(arrayShape))';  % Matlab array

end


function vector = numpyArray2vector(numpyArray)

% Convert Python numpy.ndarray to Matlab column vector
vector = double(py.array.array('d',py.numpy.nditer(numpyArray)))';

end


function numpyArray = matrix2numpyArray(matrix)

% Convert Matlab matrix to Python numpy.ndarray 
shape = fliplr(size(matrix));
matrix2 = reshape(matrix,1,numel(matrix));  % [1, n] vector
numpyArray = py.numpy.array(matrix2);
numpyArray = numpyArray.reshape(shape).transpose();  % Python ndarray

end
