import os
import fnmatch
import time
import subprocess



import socket_helper
socket_helper.get_lock('running_process_bad')


from db_settings import *
import db_helpers
import ffmpeg_helpers
import path_helpers
import string_helpers




ffmpeg_path = '/home/naz/bin/ffmpeg'

base_path = '/media/naz/6111-781C/Videodata'
src_ext = '.vid'
dst_ext = '.webm'
src_folder = "Videodata"
dst_folder = "video_compressed"


db_helpers.db_tables_init()







bad_file_model = BadFileModel.select().first()






src_file = '/media/naz/6111-781C/Videodata/10-07-2015/cam0/402.vid'


vlc_dst_dir = string_helpers.get_before_last_segment(src_file)


dst_file = path_helpers.get_dst_file(src_file, vlc_dst_dir, ext="")
# /media/naz/6111-781C/Videodata/10-07-2015/cam0/402res
dst_file = dst_file + 'res'




#
# cmd = "cvlc  " + src_file + " :sout='#transcode{vcodec=h264,venc=ffmpeg,scale=1,deinterlace}:" \
#       "std{access=file,mux=avi,dst=" + dst_file + "}'  --play-and-exit"
#
#
# subprocess.check_output(cmd, shell=True)





ff_src_file = dst_file

ff_dst_dir = path_helpers.create_dst_dirs(ff_src_file, src_folder, dst_folder)

ff_dst_file = path_helpers.get_dst_file(ff_src_file, ff_dst_dir, dst_ext)

print(ff_src_file)
print(ff_dst_file)


ffmpeg_helpers.first_pass(ffmpeg_path, ff_src_file)
ffmpeg_helpers.second_pass(ffmpeg_path, ff_src_file, ff_dst_file)







with db.atomic() as txn:
    bad_file_model.is_resolved = True
    bad_file_model.save()

    try:
        VideoModel.create(path_and_file=bad_file_model.path_and_file)
    except IntegrityError:
        print("IntegrityError: src_file exists in DB")








# while True:
#
#     model = BadFileModel.select().first()
#
#     print(model)
#
#     if not model:
#         print(model.path_and_file)




