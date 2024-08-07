#!/usr/bin/env python3

def main():
    try:
        x = int(input("Give me the first number: "))
        y = int(input("Give me the second number: "))
        print("Thank you!", "\n")
        print(f"{x} + " f"{y} = " f"{x + y}")
        print(f"{x} - " f"{y} = " f"{x - y}")
        print(f"{x} * " f"{y} = " f"{x * y}")
        print(f"{x} / " f"{y} = " f"{x / y}")
    except:
        print("Enter a valid number")

if __name__ == "__main__":
    main()