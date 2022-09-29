import re

string_length = {}


def clean_line(line):
    return line.rstrip('/n/r')


def clear_inline_commit(line):
    return re.sub(r'#.*$', '', line)


def is_comment(line):
    if line.lstrip().startswith('#'):
        return True
    return False


def is_inline_comment(line):
    if all([re.search(r'#.*$', line), not line.lstrip().startswith('#')]):
        return True
    return False


def clear_code_string(line):
    return re.sub(r'(\"|\').*(\"|\')', r'" "', line)


def clear_string(line):
    result = clear_inline_commit(line)
    return clear_code_string(result)


def check_def_class(line):
    if re.search(r'\bdef\b|\bclass\b', line):
        return line.split()[0]
    return False


def s000(line: str, number_line: int) -> bool:
    if line.isspace():
        string_length[number_line] = 0
    else:
        string_length[number_line] = len(line)
    min_len = 0
    if string_length[number_line] > min_len:
        return True
    return False


def s001(line, max_line=79):
    """ [S001] Too long """

    if len(line) > max_line:
        return 'S001'


def s002(line, number_space=4, control=0):
    """[S002] Indentation is not a multiple of four"""

    if (len(line) - len(line.lstrip())) % number_space != control:
        return 'S002'


def s003(line):
    """[S003] Unnecessary semicolon after a statement (note that semicolons are acceptable in comments)"""

    if is_comment(line):
        return False
    else:
        string = clear_string(line)
        if re.findall(r';', string):
            return 'S003'
        return False


def s004(line):
    """[S004] Less than two spaces before inline comments."""

    if is_inline_comment(line):
        if re.search(r'\s{2}#.*$', line) is None:
            return 'S004'
        return False


def s005(line):
    """[S005] TODO_ found (in comments only and case-insensitive)."""

    if any([is_comment(line), is_inline_comment(line)]):
        control = -1
        if line.lower().find('todo') == control:
            return
        return 'S005'


def s006(number_line, zero=0):
    """[S006] More than two blank lines preceding a code line (applies to the first non-empty line)."""

    if number_line > 3:
        if all([string_length[number_line - 1] == zero,
                string_length[number_line - 2] == zero,
                string_length[number_line - 3] == zero]):
            return 'S006'
    return


def s007(line):
    """[S007] Too many spaces after construction_name (def or class)."""

    if not re.match(r'\s*(\bdef\b|\bclass\b)\s\w+', line):
        return 'S007'


def s008(line):
    """[S008] Class name class_name should be written in CamelCase."""

    if not re.match(r'[A-Z]\w[^_,(,)]+', line.split()[1]):
        return 'S008', re.sub(r':', '', line.split()[1])


def s009(line):
    """[S009] Function name function_name should be written in snake_case."""

    if not re.match(r'\b[a-z0-9_]+', line.split()[1]):
        return 'S009', re.sub(r'\(.*\):', '', line.split()[1])


def checker(line, number_line):
    nl = clean_line(line)
    check_list = []
    if s000(nl, number_line):
        if s001(nl):
            check_list.append(tuple([s001(nl), None]))
        if s002(nl):
            check_list.append(tuple([s002(nl), None]))
        if s003(nl):
            check_list.append(tuple([s003(nl), None]))
        if s004(nl):
            check_list.append(tuple([s004(nl), None]))
        if s005(nl):
            check_list.append(tuple([s005(nl), None]))
        if s006(number_line):
            check_list.append(tuple([s006(number_line), None]))

        check = check_def_class(nl)
        if check:
            if s007(nl):
                check_list.append(tuple([s007(nl), check]))
            if check == 'def':
                if s009(line):
                    check_list.append(s009(line))
            elif check == 'class':
                if s008(line):
                    check_list.append(s008(line))

    return check_list
