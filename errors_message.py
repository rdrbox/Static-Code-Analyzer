errors = {
    'S001': 'Too long',
    'S002': 'Indentation is not a multiple of four',
    'S003': 'Unnecessary semicolon',
    'S004': 'At least two spaces required before inline comments',
    'S005': 'TODO found',
    'S006': 'More than two blank lines used before this line'
}


def pm(error_code, number_line):
    return f'Line {number_line}: {error_code} {errors[error_code]}'
