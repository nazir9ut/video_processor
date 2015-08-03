import subprocess

cmd = '''vlc "/home/naz/Desktop/632.vid" :sout='#transcode{vcodec=h264,venc=ffmpeg,scale=1,deinterlace}:std{access=file, mux=avi,dst="/home/naz/Desktop/tmp.avi"}' --play-and-exit'''

print(cmd)

cmd_list = cmd.split()

# print(cmd_list)

for item in cmd_list:
    print(item)

#
# subprocess.check_output(cmd_list)