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

ffmpeg_path = '/home/naz/bin/ffmpeg'




src_file = '/media/naz/6111-781C/Videodata/10-07-2015/cam0/403.vid'
dst_file = '/home/naz/PycharmProjects/video_processor/videos_src/470.webm'

ffmpeg_helpers.first_and_second_pass(ffmpeg_path, src_file, dst_file)


# 1/0
# 1st pass
# ffmpeg_helpers.first_pass(ffmpeg_path, src_file)

