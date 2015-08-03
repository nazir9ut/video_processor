import os
import fnmatch
import time

import socket_helper
socket_helper.get_lock('running_process_bad')

from db_settings import *
import db_helpers
import ffmpeg_helpers
import path_helpers


ffmpeg_path = '/home/naz/bin/ffmpeg'

base_path = '/media/naz/6111-781C/Videodata'
src_ext = '.vid'
dst_ext = '.webm'
src_folder = "Videodata"
dst_folder = "video_compressed"


db_helpers.db_tables_init()



# BadFileModel.select().where(VideoModel.path_and_file == src_file).first()