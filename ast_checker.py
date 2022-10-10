import re
import ast


def snake_case_check(string_):
    if not re.match(r'\b[a-z0-9_]+', string_):
        return False
    return True


def s008(string_):
    """[S008] Class name class_name should be written in CamelCase."""

    if not re.match(r'[A-Z]\w[^_,()]+', string_):
        return 's008'


def s009(string_):
    """[S009] Function name function_name should be written in snake_case."""

    if not snake_case_check(string_):
        return 's009'


def s010(string_):
    """[S010] Argument name arg_name should be written in snake_case."""

    if not snake_case_check(string_):
        return 's010'


def s011(string_):
    """[S011] Variable var_name should be written in snake_case."""

    if not snake_case_check(string_):
        return 's011'


def s012(argument):
    """[S012] The default argument value is mutable."""

    if isinstance(argument, (ast.List, ast.Dict, ast.Set)):
        return 's012'


def ast_checker(file):
    with open(file) as scr:
        tree = ast.parse(scr.read())
        check_list = []
        variable_list = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                if s008(class_name):
                    check_list.append(tuple([s008(class_name), class_name, node.lineno]))
            elif isinstance(node, ast.FunctionDef):
                function_name = node.name
                if s009(function_name):
                    check_list.append(tuple([s009(function_name), function_name, node.lineno]))
                for argument_name in [a.arg for a in node.args.args]:
                    if s010(argument_name):
                        check_list.append(tuple([s010(argument_name), argument_name, node.lineno]))
                        break
                for argument in node.args.defaults:
                    if s012(argument):
                        check_list.append(tuple([s012(argument), None, node.lineno]))
                        break
            elif isinstance(node, ast.Name):
                variable = node.id
                if all([s011(variable), variable not in variable_list]):
                    check_list.append(tuple([s011(variable), variable, node.lineno]))
                    variable_list.add(variable)

        return check_list
