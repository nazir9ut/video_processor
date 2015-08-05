import subprocess


def transcode(src_file, dst_file):
    try:
        cmd = "cvlc  " + src_file + " :sout='#transcode{vcodec=h264,venc=ffmpeg,scale=1,deinterlace}:" \
                                    "std{access=file,mux=avi,dst=" + dst_file + "}'  --play-and-exit"

        subprocess.check_output(cmd, shell=True)
    except:
        result = False
    else:
        result = True


    return result




