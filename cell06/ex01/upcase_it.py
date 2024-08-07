#!/usr/bin/env python3

class Greetings:
    string : str
    def upcase_it(self, string):
        return string.upper()

def main():
    x = Greetings()
    print(x.upcase_it("hello"))

if __name__ == "__main__":
    main()