#!/usr/bin/env python3

def del_dups(mylist):
    return list(set(mylist))

def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    elem = len(array)

    array = del_dups(array)
    for x in array:
        if x < 5:
            array.pop
        else:
            x += 2
            print(x, end=" ")

if __name__ == "__main__":
    main()