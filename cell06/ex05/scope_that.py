#!/usr/bin/env python3

import sys

class Math:

    nbr: int

    def add_one(self, nbr):
        return nbr + 1

def main():

    x = Math()
    nbr = 0
    print("Before add_one >", nbr)
    nbr = x.add_one(nbr)
    print("After add_one >", nbr)

if __name__ == "__main__":
    main()