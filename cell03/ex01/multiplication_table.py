#!/usr/bin/env python3

def main():
    try:
        x = int(input("Enter a number\n"))
        i = 0
        while i <= 9:
            res = x * i
            print(f"{i} x {x} = {res}")
            i += 1
    except:
        print("Enter a number!")

if __name__ == "__main__":
    main()