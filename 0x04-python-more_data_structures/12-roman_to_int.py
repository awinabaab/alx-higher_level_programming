#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    roman_numerals = {
                        "I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000
                     }
    for char in roman_string:
        if char in roman_numerals:
            result += roman_numerals[char]
    return result
