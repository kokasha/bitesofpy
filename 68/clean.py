punc = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~)'
text = "Hello. I'am here!"
def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    next_string = [x for x in input_string if x not in punc]
    # next_string = [x.replace('','') for x in input_string ]
    #print(''.join(next_string))
    return ''.join(next_string)

remove_punctuation(text)