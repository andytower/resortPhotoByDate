import os
import mimetypes
# import sys


def findAllFileInDirectory(pDir):
    for vCurDir, vSubDirs, vFiles in os.walk(pDir):
        print(f'Current dir - {vCurDir}')
        for vCurrentFile in vFiles:
            print(f'Current file - {vCurrentFile}')
            print(mimetypes.guess_type(f'{os.path.join(vCurDir,vCurrentFile)}'))
        for vCurrentSubDir in vSubDirs:
            findAllFileInDirectory(vCurrentSubDir)


if __name__ == '__main__':
    findAllFileInDirectory(os.path.join(os.getcwd(), 'unsort'))
