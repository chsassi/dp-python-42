#!/usr/bin/env python3

class Family:

    def find_the_readheads(self, dictionary: dict):
        array = []
        for keys in dictionary:
            if (dictionary.get(keys) == "Red"):
                array.append(keys)
        print(array)

def main():

    Dict = {
    "Florian": "Red",
    "Simone": "Blonde",
    "Brus": "Red",
    "Chris": "Black",
    "Sasha": "Red",
    "Jesoo": "Red",
    }

    instance = Family()
    instance.find_the_readheads(Dict)


if __name__ == "__main__":
    main()