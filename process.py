import subprocess
import numpy as np
from db_settings import *
import db_helpers
import ffmpeg_helpers
import string_helpers
import glob
import os
import fnmatch
import time



db_helpers.db_table_init()

ffmpeg_path = '/home/zhuma/bin/ffmpeg'







base_path = '/media/zhuma/6111-781C/Videodata'



matches = []
for root, dirnames, filenames in os.walk(base_path):
    filtered = fnmatch.filter(filenames, '*.vid')

    # at least 2 files with .vid extension guarantees
    # that one of them has finished recording video
    # so we can perform compression on it
    if len(filtered) >= 2:
        filtered = sorted(filtered, key = lambda filename: time.ctime(os.path.getmtime(os.path.join(root, filename))))

        del filtered[-1]


        for filename in filtered:
            matches.append(os.path.join(root, filename))









matches = np.array(matches)



for src_file in matches:
    print(src_file)
    # # 1st pass
    # ffmpeg_helpers.first_pass(ffmpeg_path, src_file)
    #
    # print('dddddddddddddddddddddddddddddddd')
    #
    # # 2nd pass
    # dst_file = '/home/naz/PycharmProjects/video_processor/videos_src/470.webm'
    # ffmpeg_helpers.second_pass(ffmpeg_path, src_file, dst_file)


# files = glob.glob(os.path.join(src_path, '*.vid'))



# for src_file in files:
#     pass
    # print(src_file)

    # print(string_helpers.get_ext(src_file))
    # print(string_helpers.get_file_name(src_file))
    #
    # print(string_helpers.get_last_segment(src_file))

    # # 1st pass
    # ffmpeg_helpers.first_pass(ffmpeg_path, src_file)
    #
    #
    # dst_file = os.path.join(dst_path, 'out1.webm')
    #
    #
    # # 2nd pass
    # ffmpeg_helpers.second_pass(ffmpeg_path, src_file, dst_file)

