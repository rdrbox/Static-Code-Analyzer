errors = {
    'S001': 'Too long',
    'S002': 'Indentation is not a multiple of four',
    'S003': 'Unnecessary semicolon',
    'S004': 'At least two spaces required before inline comments',
    'S005': 'TODO found',
    'S006': 'More than two blank lines used before this line',
    'S007': 'Too many spaces after construction_name ',
    'S008': 'Class name class_name should be written in CamelCase',
    'S009': 'Function name function_name should be written in snake_case'
}


def pm(error_code, number_line, path):
    return f'{path}: Line {number_line}: {error_code} {errors[error_code]}'
