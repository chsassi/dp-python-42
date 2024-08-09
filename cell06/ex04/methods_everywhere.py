#!/usr/bin/env python3

import sys

class String:
    string: str

    def shrink(self, string):
        string = string[:8]
        return string

    def enlarge(self, string):
        if len(string) <= 8:
            for letters in range(len(string), 8):
                string += 'Z'
        return string

def main():
    args = sys.argv[1:]
    param = String()

    for word in args:
        if len(word) > 8:
            word = param.shrink(word)
            print(word)
        elif len(word) < 8:
            word = param.enlarge(word)
            print(word)


if __name__ == "__main__":
    main()