#!/usr/bin/env python3

class RenderString:

    def render_name(self, dictionary: dict):
        array = []
        for keys in dictionary:
            array.append(keys.capitalize() + " " + dictionary[keys].capitalize())
        print(array)

def main():

    Names = {
    "christian": "sassi",
    "brus": "lutaj",
    "rick": "leone"
    }

    instance = RenderString()
    instance.render_name(Names)


if __name__ == "__main__":
    main()