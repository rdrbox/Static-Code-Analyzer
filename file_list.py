from sys import argv
import os


def base_path():
    return argv[1]


def scan_base_path(link=base_path()):
    link_list = []
    if os.path.isfile(link):
        link_list.append(os.fspath(link))
    elif os.path.isdir(link):
        for root, dirs, files in os.walk(link):
            for file in files:
                link_list.append(os.path.join(root, file))
    return tuple(link_list)


def path_file(file_name):
    return os.path.relpath(file_name)
