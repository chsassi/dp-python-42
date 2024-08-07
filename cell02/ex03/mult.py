#!/usr/bin/env python3

def main():
    try:
        x = int(input("Enter the first number\n"))
        y = int(input("Enter the second number\n"))
        res = x * y
        print(f"{x} x {y} = {res}")
        if res > 0:
            print("The result is positive")
        elif res < 0:
            print("The result is negative")
        else:
            print("The result is both positive and negative")
    except:
        print("Enter a number!")

if __name__ == "__main__":
    main()