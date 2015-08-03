import subprocess
from db_settings import *
import db_helpers
import shutil



def first_pass(ffmpeg_path, src_file):
    cmd = ffmpeg_path + " -y -i " + src_file + " -c:v libvpx-vp9 -pass 1 -b:v 1000K " \
       "-threads 8 -speed 4  -tile-columns 6 -frame-parallel 1 " \
       "-auto-alt-ref 1 -lag-in-frames 25  -an -f webm /dev/null"

    cmd_list = cmd.split()

    subprocess.check_output(cmd_list)






def second_pass(ffmpeg_path, src_file, dst_file):

    cmd = ffmpeg_path + " -i " + src_file + " -y -c:v libvpx-vp9 -pass 2 -b:v 1000K " \
           "-threads 8 -speed 1  -tile-columns 6 -frame-parallel 1 " \
           "-auto-alt-ref 1 -lag-in-frames 25  -c:a libopus -b:a 64k -f webm " + dst_file

    cmd_list = cmd.split()

    subprocess.check_output(cmd_list)





def first_and_second_pass(ffmpeg_path, src_file, dst_file, dst_dir):

    # is_bad = False
    # is_finished = True

    try:
        first_pass(ffmpeg_path, src_file)

        second_pass(ffmpeg_path, src_file, dst_file)

        try:
            VideoModel.create(path_and_file=src_file)
        except IntegrityError:
            print("IntegrityError: src_file exists in DB")

    except subprocess.CalledProcessError:
        print("CalledProcessError: cant encode video")

        try:
            BadFileModel.create(path_and_file=src_file)
        except IntegrityError:
            print("IntegrityError: src_file exists in DB")

        # copy file to dst as is
        # shutil.copy(src_file, dst_dir)

        # is_bad = True
        # is_finished = False
    else:
        print("Video encoded successfully")




