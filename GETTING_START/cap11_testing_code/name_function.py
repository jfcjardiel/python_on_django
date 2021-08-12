##first functions we are trying to test
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle == '':
        full_name = first + ' ' + last
    else:
        full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
