#!/usr/bin/env python3

def main():
    x = int(input("Give me the first number: "))
    y = int(input("Give me the second number: "))
    print("Thank you!")
    print(f"{x} + " f"{y} = " f"{x + y}")
    print(f"{x} - " f"{y} = " f"{x - y}")
    print(f"{x} / " f"{y} = " f"{x / y}")
    print(f"{x} * " f"{y} = " f"{x * y}")

if __name__ == "__main__":
    main()