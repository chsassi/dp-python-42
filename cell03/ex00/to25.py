#!/usr/bin/env python3

def main():
    try:
        x = int(input("Enter a number less than 25\n"))
        i = x
        if x > 25: 
            print("Error")
        while i <= 25:
            print("Inside the loop, my variable is "f"{i}")
            if x == 25: break
            i += 1
    except:
        print("Enter a number!")

if __name__ == "__main__":
    main()