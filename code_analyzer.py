import fileinput as fi
from file_list import path_file as pf
from file_list import scan_base_path as files
from errors_checker import checker
from errors_message import pm
from ast_checker import ast_checker as a_check

if __name__ == "__main__":
    files = files()
    line_message = []
    with fi.input(files) as f:
        for line in f:
            check_list = checker(line, fi.filelineno())
            if check_list:
                for x, y in check_list:
                    line_message.append(pm(x, fi.filelineno(), pf(fi.filename()), y))

    for file in files:
        ast_list = a_check(file)
        if ast_list:
            for x, y, z in ast_list:
                line_message.append(pm(x, z, pf(file), y))

    line_message = sorted(line_message, key=lambda point: (point[0], int(point[2])))
    for message in line_message:
        print(''.join(message))
