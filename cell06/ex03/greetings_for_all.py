#!/usr/bin/env python3

class Greetings:
    name : str

    def greetings(self, name=None):
        if name is None or name == "":
            print("Hello, noble stranger!")
        elif not isinstance(name, str):
            print("It was not a name!")
        else:
            print("Hello,", name)


def main():

    x = Greetings()
    x.greetings("Chris")
    x.greetings()
    x.greetings(42)

if __name__ == "__main__":
    main()