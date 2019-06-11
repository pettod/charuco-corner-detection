from glob import glob


def getImagesFromArguments(arguments):
    # Windows does not open file names automatically
    if isCharacterInListElements('*', arguments):
        image_names = []
        for files in arguments:
            image_names.append(glob(files))
        image_names = [item for sublist in image_names for item in sublist]

    # Linux opens file names automatically
    else:
        image_names = arguments

    return image_names


def isCharacterInListElements(character, list_):
    for elem in list_:
        if character in elem:
            return True
    return False
