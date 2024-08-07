#!/usr/bin/env python3

import sys

def main():
    param = sys.argv[1:]
    ism = "ism"

    if not param:
        print("none")
        return
    else:
        for word in param:
            if not word.endswith(ism):
                print(word + ism)

if __name__ == "__main__":
    main()
