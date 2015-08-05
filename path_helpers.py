import os
import string_helpers

# src_folder = "Videodata",
# dst_folder = "video_compressed"
def create_dst_dirs(src_file, src_folder, dst_folder):
    src_dir = string_helpers.get_before_last_segment(src_file)
    dst_dir = src_dir.replace(src_folder, dst_folder)


    try:
        os.makedirs(dst_dir)
    except OSError:
        print('OSError: Dirs exist')

    return dst_dir




# src_file = '/media/zhuma/6111-781C/Videodata/10-07-2015/cam0/401.vid'
# dst_dir = '/media/zhuma/6111-781C/video_compressed/10-07-2015/cam0'
def get_dst_file(src_file, dst_dir, ext, name_postfix = ''):
    #  bare_file_name = '401'
    bare_file_name = string_helpers.get_file_name(src_file)
    dst_file = os.path.join(dst_dir, bare_file_name + name_postfix + ext)

    return dst_file




def get_dir_of_file(file):
    result = string_helpers.get_before_last_segment(file)

    return result



