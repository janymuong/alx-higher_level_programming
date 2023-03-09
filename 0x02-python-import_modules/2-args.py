#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args_len = len(sys.argv) - 1

    if args_len == 0:
        print('{} argument{}.'.format(args_len, '' if args_len == 1 else 's'))
    else:
        print('{} argument{}:'.format(args_len, '' if args_len == 1 else 's'))

        for i in range(args_len):
            print('{}: {}'.format(i + 1, sys.argv[i + 1]))
