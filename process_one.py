import subprocess
import numpy as np
from db_settings import *
import db_helpers
import ffmpeg_helpers
import string_helpers
import path_helpers
import glob
import os
import fnmatch
import time

ffmpeg_path = '/home/zhuma/bin/ffmpeg'



db_helpers.db_tables_init()




src_file = '/media/zhuma/6111-781C/Videodata/10-07-2015/cam0/401.vid'





dst_dir = path_helpers.create_dst_dirs(src_file, "Videodata", "video_compressed")


dst_file = path_helpers.get_dst_file(src_file, dst_dir, '.webm')



ffmpeg_helpers.first_and_second_pass(ffmpeg_path, src_file, dst_file)

