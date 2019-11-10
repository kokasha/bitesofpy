from string import punctuation

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    next_string = [x for x in input_string if x not in punctuation]
    return ''.join(next_string)

