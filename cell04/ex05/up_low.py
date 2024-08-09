#!/usr/bin/env python3

def main():
    string = input()
    for element in string:
        if element.islower() == True: print(element.upper(), end="")
        elif element.isupper() == True: print(element.lower(), end="")
        else: print(element, end="")
if __name__ == "__main__":
    main()