#!/usr/bin/env python3

def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [elem + 2 for elem in array if elem >= 8]
    print(new_array)
    x = len(array)

    # print('[', end="")
    # for elem in array:
    #     if elem + 2 >= 10: print(elem + 2, end=", " if )
    # print(']', end="")

if __name__ == "__main__":
    main()