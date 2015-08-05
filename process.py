import os
import fnmatch
import time

import socket_helper
socket_helper.get_lock('running_process')

from db_settings import *
import db_helpers
import ffmpeg_helpers
import path_helpers
import config as cfg





# ffmpeg_path = '/home/naz/bin/ffmpeg'
ffmpeg_path = cfg.ffmpeg_path

# base_path = '/media/naz/6111-781C/Videodata'
base_path = cfg.base_path + cfg.src_folder

# src_ext = '.vid'
src_ext = cfg.src_ext

# dst_ext = '.webm'
dst_ext = cfg.dst_ext

# src_folder = "Videodata"
src_folder = cfg.src_folder

# dst_folder = "video_compressed"
dst_folder = cfg.dst_folder






db_helpers.db_tables_init()





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




