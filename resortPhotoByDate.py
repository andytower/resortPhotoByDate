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


def moveFile(pFileName):
    """
    Function move file in directory by date in image date create
    If dyrectory not exists it's created
    """
    try:
        vDatePhoto = get_exif(pFileName)['DateTimeOriginal'].split(' ')[0].split(':')
        vDirName = os.path.join(os.getcwd(),'resort', f'{vDatePhoto[0]}{vDatePhoto[1]}')
    except:
        vDirName = os.path.join(os.getcwd(),'resort', 'nodate')
    if not os.path.exists(vDirName):
        os.mkdir(vDirName)
        print(f'Create directory - {vDirName}')
    vNewFileName = os.path.split(pFileName)[1]
    if not os.path.exists(os.path.join(vDirName,vNewFileName)):
        with open(pFileName,'rb') as fSource:
            with open(os.path.join(vDirName,vNewFileName),'wb') as fDist:
                fDist.write(fSource.read())
                print(f'Copy file - {vNewFileName}')


def findAllFileInDirectory(pDir):
    """
    Function find all jpeg file in directory
    After finding file call function moveFile to move
    """
    for vCurDir, vSubDirs, vFiles in os.walk(pDir):
        print(f'Current dir - {vCurDir}')
        for vCurrentFile in vFiles:
            print(f'Current file - {vCurrentFile}')
            try:
                if mimetypes.guess_type(f'{os.path.join(vCurDir,vCurrentFile)}')[0].split('/')[1] == 'jpeg':
                    moveFile(os.path.join(vCurDir, vCurrentFile))
            except:
                continue
        for vCurrentSubDir in vSubDirs:
            findAllFileInDirectory(vCurrentSubDir)


if __name__ == '__main__':
    findAllFileInDirectory(os.path.join(os.getcwd(), 'unsort'))
