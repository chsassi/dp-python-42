#!/usr/bin/env python3

def main():
        psw = "fortytwo42times"
        cmp = str(input())
        if psw == cmp: print("ACCESS GRANTED")
        else: print("ACCESS DENIED")

if __name__ == "__main__":
    main()