import os
import shutil


import socket_helper
socket_helper.get_lock('running_process_bad')


from db_settings import *
import db_helpers
import ffmpeg_helpers
import path_helpers
import string_helpers
import vlc_helpers




ffmpeg_path = '/home/naz/bin/ffmpeg'

base_path = '/media/naz/6111-781C/'
src_ext = '.vid'
dst_ext = '.webm'
src_folder = "Videodata"
dst_folder = "video_compressed"
tmp_name_postfix = 'res'


db_helpers.db_tables_init()


# get first unresolved bad file from db
bad_file_model = BadFileModel.select().where(BadFileModel.is_resolved == False).first()



src_file = bad_file_model.path_and_file # /media/naz/6111-781C/Videodata/10-07-2015/cam0/402.vid


file_name = string_helpers.get_file_name(src_file) # 402


sub_path =  src_file.replace(file_name + src_ext, "")
sub_path =  sub_path.replace(base_path + src_folder + '/', "") # /10-07-2015/cam0/


final_dst_dir = os.path.join(base_path, dst_folder, sub_path) # /media/naz/6111-781C/video_compressed/10-07-2015/cam0/



print(final_dst_dir)



vlc_dst_file = os.path.join('/tmp/', file_name + tmp_name_postfix)



if vlc_helpers.transcode(src_file, vlc_dst_file):
    print('111')
    ff_src_file = vlc_dst_file
    ff_dst_dir = path_helpers.create_dst_dirs(src_file, src_folder, dst_folder)
    ff_dst_file = path_helpers.get_dst_file(ff_src_file, ff_dst_dir, dst_ext)

    if ffmpeg_helpers.first_and_second_pass_bad(ffmpeg_path, ff_src_file, ff_dst_file):
        print('111.1')
        final_dst_file = ff_dst_file
    else:
        print('000.0')
        final_dst_file = os.path.join(final_dst_dir, file_name + src_ext) #  /media/naz/6111-781C/video_compressed/10-07-2015/cam0/427.vid
        # copy file to dst as is
        shutil.copy(src_file, final_dst_dir)
else:
    print('000')
    final_dst_file = os.path.join(final_dst_dir, file_name + src_ext) #  /media/naz/6111-781C/video_compressed/10-07-2015/cam0/427.vid
    # copy file to dst as is
    shutil.copy(src_file, final_dst_dir)











with db.atomic() as txn:
    bad_file_model.is_resolved = True
    bad_file_model.save()

    try:
        VideoModel.create(path_and_file=bad_file_model.path_and_file)
    except IntegrityError:
        print("IntegrityError: src_file exists in DB")








