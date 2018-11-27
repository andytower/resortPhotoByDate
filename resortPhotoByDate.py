import os
import mimetypes
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(p_file_name):
    """
    Function return all EXIF Tags from file
    """
    ret = {}
    i = Image.open(p_file_name)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def move_file(p_file_name):
    """
    Function move file in directory by date in image date create
    If directory not exists it's created
    """
    try:
        v_date_photo = get_exif(p_file_name)['DateTimeOriginal'].split(' ')[0].split(':')
        v_dir_name = os.path.join(os.getcwd(), 'resort', f'{v_date_photo[0]}{v_date_photo[1]}')
    except:
        v_dir_name = os.path.join(os.getcwd(), 'resort', 'nodate')
    if not os.path.exists(v_dir_name):
        os.mkdir(v_dir_name)
        print(f'Create directory - {v_dir_name}')
    v_new_file_name = os.path.split(p_file_name)[1]
    if not os.path.exists(os.path.join(v_dir_name, v_new_file_name)):
        with open(p_file_name, 'rb') as fSource:
            with open(os.path.join(v_dir_name, v_new_file_name), 'wb') as fDist:
                fDist.write(fSource.read())
                print(f'Copy file - {v_new_file_name}')


def copy_other_files(p_file_name):
    """
    Function copy no photo file in directory resort/others
    """
    v_dir_name = os.path.join(os.getcwd(), 'resort', 'others')
    if not os.path.exists(v_dir_name):
        os.mkdir(v_dir_name)
    v_new_file_name = os.path.split(p_file_name)[1]
    if not os.path.exists(os.path.join(v_dir_name, v_new_file_name)):
        with open(p_file_name, 'rb') as fSource:
            with open(os.path.join(v_dir_name, v_new_file_name), 'wb') as fDist:
                fDist.write(fSource.read())
                print(f'Copy file - {v_new_file_name}')


def find_all_file_in_directory(p_dir):
    """
    Function find all jpeg file in directory
    After finding file call function moveFile to move
    """
    for v_cur_dir, v_sub_dirs, v_files in os.walk(p_dir):
        print(f'Current dir - {v_cur_dir}')
        for v_current_file in v_files:
            print(f'Current file - {v_current_file}')
            try:
                if mimetypes.guess_type(f'{os.path.join(v_cur_dir, v_current_file)}')[0].split('/')[1] == 'jpeg':
                    move_file(os.path.join(v_cur_dir, v_current_file))
                else:
                    copy_other_files(os.path.join(v_cur_dir, v_current_file))
            except:
                copy_other_files(os.path.join(v_cur_dir, v_current_file))
                continue
        for v_current_sub_dir in v_sub_dirs:
            find_all_file_in_directory(v_current_sub_dir)


if __name__ == '__main__':
    find_all_file_in_directory(os.path.join(os.getcwd(), 'unsort'))
