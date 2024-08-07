#!/usr/bin/env python3

import sys

def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("none")
    elif len(args) > 2:
        for args in reversed(args):
            print(args)

if __name__ == "__main__":
    main()
