#!/usr/bin/env python3

import sys

def main():
    param = sys.argv[1:]
    
    if len(param) != 1:
        print("none")
        return

    inp_str = str(input("What was the parameter?: "))
    if inp_str == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()
