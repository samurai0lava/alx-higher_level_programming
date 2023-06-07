#!/bin/bash/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string

    # Create a list from the string to make it mutable
    chars = list(string)

    # Remove the character at index n
    del chars[n]

    # Convert the list back to a string
    new_string = ''.join(chars)

    return new_string

