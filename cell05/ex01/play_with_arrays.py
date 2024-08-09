#!/usr/bin/env python3

def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [elem + 2 for elem in array if elem >= 8]
    x = len(array)

    print('[ ', end="")
    for elem in array:
        print(elem + 2, end=" ")
    print(']', end="")

if __name__ == "__main__":
    main()