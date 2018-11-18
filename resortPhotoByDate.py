import os
import mimetypes
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(vFileName):
    """
    Function return all EXIF Tags from file
    """
    ret = {}
    i = Image.open(vFileName)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def moveFile(vFileName):
    """
    Function move file in directory by date in image date create
    """
    vDatePhoto = get_exif(vFileName)['DateTimeOriginal'].split(' ')[0].split(':')
    vNewFileName = os.path.join(os.getcwd(),'sort', f'{vDatePhoto[0]}{vDatePhoto[1]}', os.path.split(vFileName)[1])
    print(vNewFileName)


def findAllFileInDirectory(pDir):
    """
    Function find all jpeg file in directory
    After finding file call function moveFile to move
    """
    for vCurDir, vSubDirs, vFiles in os.walk(pDir):
        print(f'Current dir - {vCurDir}')
        for vCurrentFile in vFiles:
            print(f'Current file - {vCurrentFile}')
            if mimetypes.guess_type(f'{os.path.join(vCurDir,vCurrentFile)}')[0].split('/')[1] == 'jpeg':
                moveFile(os.path.join(vCurDir, vCurrentFile))
        for vCurrentSubDir in vSubDirs:
            findAllFileInDirectory(vCurrentSubDir)


if __name__ == '__main__':
    findAllFileInDirectory(os.path.join(os.getcwd(), 'unsort'))
