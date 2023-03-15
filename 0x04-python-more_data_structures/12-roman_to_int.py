#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
    converts a Roman numeral to an integer
    for 1 to 3999
    '''
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if roman_string and type(roman_string) == str:
        result = 0
        prev_value = 0

        for i in range(len(roman_string)-1, -1, -1):
            int_val = roman_numbers[roman_string[i]]

            if int_val >= prev_value:
                result += int_val
            else:
                result -= int_val

            prev_value = int_val

        return result
    else:
        return 0
