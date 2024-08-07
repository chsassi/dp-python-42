#!/usr/bin/env python3

import math

def main():
    nbr = float(input("Give me a number: "))
    try:
        print(math.ceil(nbr))
    except:
        print("Enter a number")

if __name__ == "__main__":
    main()