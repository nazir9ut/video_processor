import os


# file: like /home/naz/PycharmProjects/video_processor/videos_src/408.vid
def get_ext(file):
    file_name, file_extension = os.path.splitext(file)

    return file_extension


# file: like /home/naz/PycharmProjects/video_processor/videos_src/408.vid
# return "408"
def get_file_name(file):
    # file_name becomes "/home/naz/PycharmProjects/video_processor/videos_src"
    file_name, file_extension = os.path.splitext(file)

    file_name = get_last_segment(file_name)

    return file_name



# file: like /home/naz/PycharmProjects/video_processor/videos_src/408.vid
def get_last_segment(file):
    result = file.rsplit('/',1)[-1]

    return result


# file: like /home/naz/PycharmProjects/video_processor/videos_src/408.vid
def get_before_last_segment(file):
    result = file.rsplit('/',1)[0]

    return result