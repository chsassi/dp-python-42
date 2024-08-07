#!/usr/bin/env python3

class Greetings:
    name : str
    def greetings(self, name):
        if not isinstance(name, str):
            print("It was not a name!")
        elif name == "" or not name:
            print("Hello, noble stranger!")
        else:
            print("Hello,", name)


def main():

    x = Greetings()
    # Greetings.greetings("Christian")
    x.greetings("Rick")

if __name__ == "__main__":
    main()