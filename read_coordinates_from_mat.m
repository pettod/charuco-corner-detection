function [imCorners, imIds] = read_coordinates_from_mat(maxNumberOfCorners, numberOfImages)

% Read checkerboard corners and corner IDs
charucoCornersXY = load('coords.mat');
cornerIds = load('ids.mat');

% Get image names
cornerFields = fieldnames(charucoCornersXY);
idFields = fieldnames(cornerIds);

% Read all images if numberOfImages == -1
if numberOfImages == -1
    numberOfImages = numel(cornerFields);
end

imCorners = zeros(maxNumberOfCorners, 2, numberOfImages);
imIds = zeros(numberOfImages, maxNumberOfCorners);

% Loop all images
for i = 1:numberOfImages
    corners = charucoCornersXY.(cornerFields{i});
    ids = cornerIds.(idFields{i});
    missingNumberOfCorners = maxNumberOfCorners - length(ids);
    
    % Add -1 to the end
    cornersFilled = [corners; -1*ones(missingNumberOfCorners, 2)];
    idsFilled = [ids -1*ones(1, missingNumberOfCorners)];
    
    % Add corners and ids to data structure
    imCorners(:, :, i) = cornersFilled;
    imIds(i, :) = idsFilled; 
end

end