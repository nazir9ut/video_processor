import os
import fnmatch
import time

from db_settings import *
import db_helpers
import ffmpeg_helpers
import string_helpers
import path_helpers






ffmpeg_path = '/home/zhuma/bin/ffmpeg'


base_path = '/media/zhuma/6111-781C/Videodata'
src_ext = '.vid'
dst_ext = '.webm'
src_folder = "Videodata"
dst_folder = "video_compressed"





db_helpers.db_tables_init()


matches = []
for root, dirnames, filenames in os.walk(base_path):
    filtered = fnmatch.filter(filenames, '*' + src_ext)

    # at least 2 files with .vid extension guarantees
    # that at least one of them has finished recording video
    if len(filtered) >= 2:

        filtered = sorted(filtered, key = lambda filename: time.ctime(os.path.getmtime(os.path.join(root, filename))))

        # del filtered[-1]

        for filename in filtered:
            src_file = os.path.join(root, filename)
            exists = VideoModel.select().where(VideoModel.path_and_file == src_file).exists()

            if not exists:
                dst_dir = path_helpers.create_dst_dirs(src_file, src_folder, dst_folder)

                dst_file = path_helpers.get_dst_file(src_file, dst_dir, dst_ext)

                ffmpeg_helpers.first_and_second_pass(ffmpeg_path, src_file, dst_file, dst_dir)




