# File called "adieu.py"
# Prompt for names until they break (with control-d or ctlr-z)
# Assume at least one name
# "Adieu, Adieu, to..." enter all names separated by ","
# INPUTS should be stored in a list
# ITTERATE through the list for the PRINT functions

import sys


def main():
    names = []
    while True:
        try:
            user_input = input()
            names.append(user_input)
        except EOFError:
            print(print_response(names))
            sys.exit()


def print_response(list):
    list_len = len(list)
    adieu = "Adieu, adieu, to "
    if list_len == 2:
        return f"{adieu}{list[0]} and {list[1]}"
    else:
        names = ", ".join(list)
        if list_len > 2:
            names = names.rsplit(", ", maxsplit=1)
            names = str(f"{names[0]}, and {names[1]}")
            return adieu + names
        else:
            return adieu + names


if __name__ == "__main__":
    main()
