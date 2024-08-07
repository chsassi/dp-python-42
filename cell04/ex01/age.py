#!/usr/bin/env python3

def main():
    try:
        age = int(input("Please tell me your age: "))
        print("You're currently " f"{age} years old\nIn ten years, you'll be " f"{age + 10} years old\nIn twenty years, you'll be " f"{age + 20} years old\nIn thirty years, you'll be " f"{age + 30} years old\n")
    except:
        print("Enter a number.")

if __name__ == "__main__":
    main()