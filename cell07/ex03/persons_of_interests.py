#!/usr/bin/env python3

class Scientists:

    def famous_births(self, dictionary: dict):
        for key, value in dictionary.items():
            name = value['name']
            dob = value['date_of_birth']
            print(f"{name} is a scientist born in " f"{dob}")

def main():

    Women_Scientists = {
    "Ada": {"name": "Ada Lovelance", "date_of_birth": 1815}, 
    "Cecilia": {"name": "Cecilia Payne", "date_of_birth": 1878},
    "Lise": {"name": "Lise Meitner", "date_of_birth": 1900},
    "Grace": {"name": "Grace Hopper", "date_of_birth": 1906},
    }

    instance = Scientists()
    instance.famous_births(Women_Scientists)

if __name__ == "__main__":
    main()