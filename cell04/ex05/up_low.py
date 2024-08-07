#!/usr/bin/env python3

def main():
    string = input()
    for element in string:
        if str(element).islower() == True: print(element.upper(), end="")
        elif str(element).isupper() == True: print(element.lower(), end="")

if __name__ == "__main__":
    main()