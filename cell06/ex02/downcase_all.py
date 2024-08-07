#!/usr/bin/env python3

import sys

class Greetings:
    string : str
    def downcase_all(string):
        return string.lower()

def main():
    args = sys.argv[1:]

    for words in args:
        print(Greetings.downcase_all(words))

if __name__ == "__main__":
    main()