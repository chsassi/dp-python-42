#!/usr/bin/env python3

import statistics

class Class:

    def average(self, dictionary: dict):
        n_average = []
        for keys in dictionary:
            n_average.append(dictionary[keys])
        return (statistics.mean(n_average))

def main():

    Assignment1 = {
    "Florian": 18, 
    "Simone": 20,
    "Brus": 27,
    "Chris": 27,
    "Sasha": 28,
    "Giulio": 29
    }

    Assignment2 = {
    "Florian": 28, 
    "Simone": 21,
    "Brus": 27,
    "Chris": 27,
    "Sasha": 29,
    "Giulio": 30
    }

    instance = Class()
    print("Average for Assignment1: " f"{instance.average(Assignment1)}")
    print("Average for Assignment2: " f"{instance.average(Assignment2)}")


if __name__ == "__main__":
    main()