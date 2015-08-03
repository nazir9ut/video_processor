import subprocess


src_file = '/home/naz/Desktop/427.vid'
dst_file = '/home/naz/Desktop/tmp.avi'


cmd = "cvlc  " + src_file + " :sout='#transcode{vcodec=h264,venc=ffmpeg,scale=1,deinterlace}:" \
      "std{access=file,mux=avi,dst=" + dst_file + "}'  --play-and-exit"



print(cmd)


cmd_list = cmd.split()



for item in cmd_list:
    print(item)


res = subprocess.check_output(cmd, shell=True)

# print(res)