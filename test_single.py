import os
import time

import socket_helper





socket_helper.get_lock('running_test')



while True:

    time.sleep(1)


    pid = os.getpid()

    print(pid)

    with open('/home/zhuma/PycharmProjects/video_processor/somefile.txt', 'a') as the_file:

        the_file.write(str(pid) + '\n')