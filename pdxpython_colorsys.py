def rgb_to_hex(rgb):
    """
    Converts a RGB tuple into a HTML hex color.
    RGB values are between 0 and 255.
    
    >>> rgb_to_hex(255, 0, 255)
    '#ff00ff'
    >>> rgb_to_hex(123, 231, 123)
    """
    hex = "#" + ''.join("%02x" % x for x in rgb)
    return hex
    
def hex_to_rgb(hex):
    """
    Converts a HTML hex color into a RGB tuple. 
    >>> hex_to_rgb('#ff00ff')
    (255, 0, 255)
    >>> hex_to_rgb('f0f')
    (255, 0, 255)
    """
    hex = hex[1:] if hex[0] else hex
    return tuple(int(hex[x:x+2], 16) for x in range(0, len(hex), 2))
