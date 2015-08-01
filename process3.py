import subprocess


ffmpeg_path = '/home/naz/bin/ffmpeg'
src_path_and_file = '/home/naz/PycharmProjects/video_processor/videos/470.vid'
dst_path_and_file = '/home/naz/PycharmProjects/video_processor/videos/out3.webm'




# 1st pass

cmd = ffmpeg_path + " -y -i " + src_path_and_file + " -c:v libvpx-vp9 -pass 1 -b:v 1000K " \
       "-threads 8 -speed 4  -tile-columns 6 -frame-parallel 1 " \
       "-auto-alt-ref 1 -lag-in-frames 25  -an -f webm /dev/null"

cmd_list = cmd.split()

subprocess.check_output(cmd_list)


print('1st pass done')





# 2nd pass

cmd = ffmpeg_path + " -i " + src_path_and_file + " -y -c:v libvpx-vp9 -pass 2 -b:v 1000K " \
       "-threads 8 -speed 1  -tile-columns 6 -frame-parallel 1 " \
       "-auto-alt-ref 1 -lag-in-frames 25  -c:a libopus -b:a 64k -f webm " + dst_path_and_file

cmd_list = cmd.split()

a = subprocess.check_output(cmd_list)


print('2nd pass done')
