#!/usr/bin/env python3

import sys

def main():
    params = len(sys.argv)
    if not params or params == 1:
        print("none")
    else:
        string = sys.argv[1]
        print(string)

if __name__ == "__main__":
    main()