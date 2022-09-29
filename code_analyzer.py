import fileinput as fi
from file_list import path_file as pf
from file_list import scan_base_path as files
from errors_checker import checker
from errors_message import pm

if __name__ == "__main__":

    files = files()
    with fi.input(files) as f:
        for line in f:
            check_list = checker(line, fi.filelineno())
            if check_list:
                line_message = []
                for x, y in check_list:
                    line_message.append(pm(x, fi.filelineno(), pf(fi.filename()), y))
                line_message.sort()
                for message in line_message:
                    print(message)
