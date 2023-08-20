#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Convert a Roman numeral string to an integer.

    Parameters:
    - roman_string (str): The Roman numeral string to be converted.

    Returns:
    - int: The integer representation of the Roman numeral string.
    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_val = 0

    if not isinstance(roman_string, str) or None:
        return 0

    for i in range(len(roman_string)):
        if i > 0 and roman[roman_string[i]] > roman[roman_string[i - 1]]:
            num_val += roman[roman_string[i]] - 2 * roman[roman_string[i - 1]]
        else:
            num_val += roman[roman_string[i]]

    return num_val
