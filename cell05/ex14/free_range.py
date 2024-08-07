#!/usr/bin/env python3

import sys

def main():
    params = (len(sys.argv) - 1)

    if not params or params != 2:
        print("none")
    else:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            if start <= end:
                array = list(range(start, end + 1))
                for number in array:
                    print(number, end=" ")
            else:
                array = list(range(end, start + 1))
                for number in array:
                    print(number, end=" ")
        except ValueError:
            print("none")

if __name__ == "__main__":
    main()

########>
#def main():
#     params = (len(sys.argv) - 1)

#     if not params or params != 2:
#         print("none")
#     else:
#         minimum = int(sys.argv[1])
#         maximum = int(sys.argv[2])
#         if minimum < maximum:
#             while minimum <= maximum:
#                 print(minimum)
#                 minimum += 1
#         else:
#             while minimum >= maximum:
#                 print(minimum)
#                 minimum -= 1

# if __name__ == "__main__":
#     main()