#!/usr/bin/env python3

import sys

def main():
    args = sys.argv[1:]
    
    if len(args) != 2:
        print("none")
        return

    to_find = args[0]
    search_string = args[1]
    count = search_string.count(to_find)

    if not count:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()
