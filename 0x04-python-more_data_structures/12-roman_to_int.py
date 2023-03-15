#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
    converts a Roman numeral to an integer
    for 1 to 3999
    '''
    roman_values = {
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
            current_value = roman_values[roman_string[i]]

            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value

            prev_value = current_value

        return result
    else:
        return 0
