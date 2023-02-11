def capitalize(text):
    first, *other = text
    return f'{first.upper()}{"".join(other)}'
