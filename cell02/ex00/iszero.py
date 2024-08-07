#!/usr/bin/env python3

def main():
    try:
        x = int(input())
        if x > 0: print("This number is different from zero.")
        elif x == 0: print("This number is equal to zero.")
    except:
        print("Enter a number!")

if __name__ == "__main__":
    main()