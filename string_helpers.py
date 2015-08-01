import os


# file: like /home/naz/PycharmProjects/video_processor/videos_src/408.vid
def get_ext(file):
    file_name, file_extension = os.path.splitext(file)

    return file_extension


# file: like /home/naz/PycharmProjects/video_processor/videos_src/408.vid
def get_file_name(file):
    file_name, file_extension = os.path.splitext(file)

    return file_name



# file: like /home/naz/PycharmProjects/video_processor/videos_src/408.vid
def get_last_segment(file):
    result = file.rsplit('/',1)[-1]

    return result