#!/usr/bin/python3
'''reads stdin line by line and computes metrics:'''

import sys


def print_metrics(status_codes, total_size):
    '''
    Print the computed metrics
    '''

    print(f'File size: {total_size}')
    for err_code in sorted(status_codes.keys()):
        if status_codes[err_code]:
            print(f'{err_code}: {status_codes[err_code]}')


def parse_line(line):
    '''
    Parse a line and return its characters
    '''

    char_seq = line.split()
    return char_seq[-2], int(char_seq[-1])


def main():
    '''status codes dict'''
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        for i, line in enumerate(sys.stdin, start=1):
            code, size = parse_line(line)
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
            if i % 10 == 0:
                print_metrics(status_codes, total_size)

    except KeyboardInterrupt:
        print_metrics(status_codes, total_size)
        raise


if __name__ == '__main__':
    main()
