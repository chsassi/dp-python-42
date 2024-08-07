#!/usr/bin/env python3

def main():
    try:
        x = int(input())
        if x > 0: print("This number is positive.")
        elif x == 0: print("This number is both positive and negative.")
        else: print("This number is negative.")
    except:
        print("Enter a number!")

if __name__ == "__main__":
    main()