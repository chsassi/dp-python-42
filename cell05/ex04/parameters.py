#!/usr/bin/env python3

import sys

def main():
    params = len(sys.argv)
    print("Numbers of parameters: " f"{params - 1}")

if __name__ == "__main__":
    main()