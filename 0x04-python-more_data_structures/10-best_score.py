#!/usr/bin/python3

def best_score(a_dictionary):
    # Ckecks if dictionary is None
    if a_dictionary is None:
        return None

    # Use dictionary comprehension to create a new dictionary with keys as values and values as keys
    new_dict = {value: key for key, value in a_dictionary.items() if isinstance(value, int)}

    # Check if new_dictionary is empty
    if not new_dict:
        return None

    max_value = max(a_dictionary.values())

    # Return the key with the maximum value in the inverted dictionary
    max_key = new_dict[max_value]

    return max_key
