def capitalize(text):
    if text == '':
        return ''
    first, *other = text
    return f'{first.upper()}{"".join(other)}'

