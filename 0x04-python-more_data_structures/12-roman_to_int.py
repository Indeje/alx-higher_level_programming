#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    decimal = 0
    index = 0
    for char in roman_string.upper():
        if char == 'M':
            decimal += 1000
        elif char == 'D':
            decimal += 500
        elif char == 'C':
            try:
                if roman_string[index + 1] in "DM":
                    decimal -= 100
                else:
                    decimal += 100
            except IndexError:
                decimal += 100
        elif char == 'L':
            decimal += 50
        elif char == 'X':
            try:
                if roman_string[index + 1] in "LC":
                    decimal -= 10
                else:
                    decimal += 10
            except IndexError:
                decimal += 10
        elif char == 'V':
            decimal += 5
        elif char == 'I':
            try:
                if roman_string[index + 1] in 'XV':
                    decimal -= 1
                else:
                    decimal += 1
            except IndexError:
                decimal += 1

        index += 1
    return decimal
