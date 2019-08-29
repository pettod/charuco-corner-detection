function [imCorners, imIds] = ...
    read_corners_from_mat(maxBoardCorners, numberOfImages, ...
    cornersFileName, idsFileName)

% Read checkerboard corners and corner IDs
charucoCornersXY = load(cornersFileName);
cornerIds = load(idsFileName);

% Get image names
cornerFields = fieldnames(charucoCornersXY);
idFields = fieldnames(cornerIds);

% Read all images if numberOfImages == -1
if numberOfImages == -1
    numberOfImages = numel(cornerFields);
end

imCorners = zeros(maxBoardCorners, 2, numberOfImages);
imIds = zeros(numberOfImages, maxBoardCorners);

% Loop all images
for i = 1:numberOfImages
    corners = charucoCornersXY.(cornerFields{i});
    ids = cornerIds.(idFields{i});
    missingNumberOfCorners = maxBoardCorners - length(ids);
    
    % Add -1 to the end
    cornersFilled = [corners; -1*ones(missingNumberOfCorners, 2)];
    idsFilled = [ids -1*ones(1, missingNumberOfCorners)];
    
    % Add corners and ids to data structure
    imCorners(:, :, i) = cornersFilled;
    imIds(i, :) = idsFilled; 
end

end