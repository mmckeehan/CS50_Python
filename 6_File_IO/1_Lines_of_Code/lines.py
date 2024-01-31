import sys
import fileinput


def main():
    name = file_name()
    count_line = 0
    # Takes the total lines for count_lines
    try:
        with fileinput.input(files=name) as file:
            for line in file:
                count_line = +fileinput.lineno()
        # Removes comments and whitespace from count_lines
        with fileinput.input(files=name) as file:
            for line in file:
                if line.strip().startswith("#"):
                    count_line -= 1
                elif line.isspace():
                    count_line -= 1
                else:
                    None
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(count_line)


def file_name():
    try:
        fn = sys.argv[1]
        # Checks to see if there is only one file
        if len(sys.argv) == 2:
            if is_python(fn):
                return fn
            else:
                sys.exit("Not a Python file")
        else:
            sys.exit("Too many command-line arguments")
    except IndexError:
        # Return if there is no file entered.
        sys.exit("Too few command-line arguments.")


# Checks ".py" file type
def is_python(fn):
    if fn.endswith(".py"):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
