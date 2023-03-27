#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''safe - prints x elements of a list'''

    len_list = 0
    try:
        for i in range(x):
            print('{}'.format(my_list[i]), end='')
            len_list += 1
    except IndexError:
        pass
    finally:
        print('')
        return len_list
