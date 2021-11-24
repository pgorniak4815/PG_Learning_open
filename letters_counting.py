"""
Ex. 1 Hw. 1 from "Using Python for Research" course.

The task is to build a function that counts each letter in sentences
and to test it.
"""

def counter(input_string):
    """
    This function count and return occurrence of individual\n letters in given sentence
    """
    count_letters = {}
    input_string = input_string.replace(" ","")

    for item in input_string:
        if item in count_letters:
            count_letters[item] = count_letters[item] + 1
        else:
            count_letters[item] = 1
    return count_letters


sentence = 'Jim quickly realized that the beautiful gowns are expensive'

print(counter(sentence))
help(counter)
