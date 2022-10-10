errors = {
    's001': 'Too long',
    's002': 'Indentation is not a multiple of four',
    's003': 'Unnecessary semicolon',
    's004': 'At least 2 spaces required before inline comments',
    's005': 'TODO found',
    's006': 'More than two blank lines used before this line',
    's007': 'Too many spaces after "{}"',
    's008': 'Class name "{}" should be written in CamelCase',
    's009': 'Function name "{}" should be written in snake_case',
    's010': 'Argument name "{}" should be written in snake_case',
    's011': 'Variable "{}" should be written in snake_case',
    's012': 'The default argument value is mutable'
}


def pm(error_code, number_line, path, scope=None):
    return [f'{path}:', ' line ', f'{number_line}', f': {error_code} {errors[error_code].format(scope)}']
