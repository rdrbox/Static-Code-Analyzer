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


def checker(line, number_line):
    nl = clean_line(line)
    check_list = []
    if s000(nl, number_line):
        if s001(nl):
            check_list.append(s001(nl))
        if s002(nl):
            check_list.append(s002(nl))
        if s003(nl):
            check_list.append(s003(nl))
        if s004(nl):
            check_list.append(s004(nl))
        if s005(nl):
            check_list.append(s005(nl))

        if s006(number_line):
            check_list.append(s006(number_line))

    return check_list
