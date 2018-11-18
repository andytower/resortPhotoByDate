import os
import mimetypes


def findAllFileInDirectory(pDir):
    for vCurDir, vSubDirs, vFiles in os.walk(pDir):
        print(f'Current dir - {vCurDir}')
        for vCurrentFile in vFiles:
            print(f'Current file - {vCurrentFile}')
            if mimetypes.guess_type(f'{os.path.join(vCurDir,vCurrentFile)}')[0].split('/')[1] == 'jpeg':
                print('This is jpeg')
        for vCurrentSubDir in vSubDirs:
            findAllFileInDirectory(vCurrentSubDir)


if __name__ == '__main__':
    findAllFileInDirectory(os.path.join(os.getcwd(), 'unsort'))
