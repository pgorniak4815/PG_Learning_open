"""
Ex. 1 Hw. 3 from "Using Python for Research" course.

The task is to build a function to encode message by Cesar 
cipher. 
"""
import string


def encoding(message, key=0):
    """
    Each letter in a message is shifted by a few (key)
    characters in the alphabet, and returned.
    """
    alphabet = " " + string.ascii_lowercase

    positions = {}
    n = 0
    for item in alphabet:
        positions.update({item: n})
        n += 1

    encoding_list = []
    for char in message:
        position = positions[char]
        encoded_position = (position + key) % 27
        encoding_list.append(alphabet[encoded_position])
    encoded_string = "".join(encoding_list)
    return encoded_string

# test
message = "hi my name is caesar"

encoded_message = encoding(message, 3)
print(encoded_message)

decoded_message = encoding(encoded_message, -3)
print(decoded_message)
