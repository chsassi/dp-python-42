#!/usr/bin/env python3

def isFloat(num):
    return num != int(num)

def main():
    nbr = float(input("Give me a first number: "))
    try:
        float(nbr)
        if isFloat(nbr):
            print("The number is a decimal")
        else:
            int(nbr)
            print("The number is an integer")
    except ValueError:
        print("Enter a valid number")

if __name__ == "__main__":
    main()