#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for name in range(len(dir(hidden_4))):
        if dir(hidden_4)[name][:2] != '__':
            print('{:s}'.format(dir(hidden_4)[name]))
