"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""
    hex_dict = {"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    
    new_list = list(hex_in)
    total = 0
    counter = 0

    for i in range((len(new_list)-1),-1,-1):

        if new_list[counter].isdigit():
            num = int(new_list[counter])
        else:
            key = new_list[counter].lower()
            num = hex_dict[key]

        calc = num * (16 ** i)
        total += calc

        counter += 1

    return total


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n")
