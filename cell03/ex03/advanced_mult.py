#!/usr/bin/env python3

def adv_mult():
    i = 0
    while i <= 10:
        print(f"{i} Times Table: ", end="")
        j = 0
        while j <= 10:
            print(f"{i * j}", end=" ")
            j += 1
        print()
        i += 1

def main():
    adv_mult()

if __name__ == "__main__":
    main()
