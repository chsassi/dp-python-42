#!/usr/bin/env python3

import sys

def main():
    params = sys.argv[1:]

    if not params:
        print("none")
        return
    else:
        print(f"parameters: {len(params)}")
        for elem in params:
            string = sys.argv[1:]
            strlen = len(string)
            print(f"{elem}: {len(elem)}")

if __name__ == "__main__":
    main()
