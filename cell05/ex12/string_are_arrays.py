#!/usr/bin/env python3

import sys

def main():
    param = sys.argv[1]
    char = 'z'

    if not param:
        print("none")
        return
    else:
        for letter in param:
            if letter == char: print("z", end="")


if __name__ == "__main__":
    main()
