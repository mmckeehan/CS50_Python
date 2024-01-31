# File called "figlet.py"
# Expects '0' or '2' cmd line args as input
# '0' to enter input into the program
# '2' to enter cmd args
# if the first arg is not '-f' or '--font', exit via "sys.exit"
# if the second arg is not the font, exit via "sys.exit"

import sys
import pyfiglet


def main():
    figlet = pyfiglet.Figlet
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            f_type = sys.argv[2]
            check_font(f_type)
            user_input = input("Input: ")
            mod_text(user_input, f_type)
        else:
            sys.exit("Incorrect Arugments")

    elif len(sys.argv) == 1:
        user_input = input("Input: ")
        f_type = input("Style: ")
        check_font(f_type)
        mod_text(user_input, f_type)
    else:
        sys.exit("Incorrect Arugments")



def check_font(font):
    if font in pyfiglet.FigletFont.getFonts():
        return font
    else:
        sys.exit("Incorrect Arugments")


def mod_text(ui, ft):
    f = pyfiglet.Figlet(font=ft)
    print(f.renderText(ui))


if __name__ == "__main__":
    main()
