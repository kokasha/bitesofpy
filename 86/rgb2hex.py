def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    r, g, b = rgb
    if (r or g or b) not in range(0,256):
       raise ValueError
    print('#{:02x}{:02x}{:02x}'.format(r,g,b).upper())
    return '#{:02x}{:02x}{:02x}'.format(r,g,b).upper()

rgb_to_hex((2,4,255))