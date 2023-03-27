#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists
    return: new list with all divisions
    """
    final_list = []

    for i in range(list_length):
        try:
            div_re = 0
            if i < len(my_list_1):
                if i < len(my_list_2):
                    div_re = my_list_1[i] / my_list_2[i]
                else:
                    print(f'out of range')
            else:
                print(f'out of range')
        except TypeError:
            print(f'wrong type')
        except ZeroDivisionError:
            print(f'division by 0')
        finally:
            final_list.append(div_re)

    return final_list
