import os


def get_file_list(file_path):

    files = []
    for root, dirs, files in os.walk(file_path):
        print('# of files: {0}'.format(len(files)))  # can be "pass"
    file_list = files
    return file_list
