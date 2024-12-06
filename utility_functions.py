"""file containing utility functions"""

def lowercase(s : str) -> str :
    """
    Returns the lowercase version of a string
    :param s: string to be lowercased
    :return: lowercase version of the string
    """
    # instantiation of string to be returned
    ns = ""

    # iteration over s
    for c in s:
        # test of position of current char relative to uppercase bounds (A & Z)
        if ord('A') <= ord(c) <= ord('Z'):
            # concatenation of lowercase-converted current char to string
            ns += chr(ord(c) + (ord('a') - ord('A')))
        else :
            # concatenation of current car to string
            ns += c
    return ns