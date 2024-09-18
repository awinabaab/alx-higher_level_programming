#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        result = 0
        curr_value = 0
        prev_value = 0
        roman_numerals = {
                            "I": 1,
                            "V": 5,
                            "X": 10,
                            "L": 50,
                            "C": 100,
                            "D": 500,
                            "M": 1000
                         }
        for char in reversed(roman_string):
            curr_value = roman_numerals[char]
            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value
            prev_value = curr_value
        return result
    else:
        return 0
