#!/usr/bin/env python3

import sys

def main():
    params = len(sys.argv)

    if not params or params == 1:
        print("none")
    elif params > 1:
        for elem in sys.argv[1:]:
            elem = elem.lower()
            print(elem)

if __name__ == "__main__":
    main()