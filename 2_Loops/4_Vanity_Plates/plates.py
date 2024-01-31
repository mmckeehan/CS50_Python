def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if verify(s) and begin(s) and number(s): return True

# Checks to see if the plate is all real numbers and is the correct length
def verify (v):
    if v.isalnum() and count(v):
        #debug(1)
        return True
    else:
        #debug(2)
        return False

# Checks to see if the plate is between two and 6 characters
def count(l):
    if 2 <= len(l) <= 6: return True

# Checks to see if the first two digits are letters
def begin (b):
    if b[0] and b[1].isalpha():
        #debug(3)
        return True
    else:
        #debug(4)
        return False


# Checks to see if there is any letters between numbers
def number(n):
    if n.isalpha():
        #debug(5)
        return True
    elif check_zero(n):
        if check_letters(n):
            return True
        else:
            return False

# Checks to see if the first number in the string is "0"
def check_zero(z):
    ztest = z.split("0")
    if ztest[0].isalpha():
        #debug(6)
        return False
    else:
        #debug(7)
        return True

# Checking to see if there are any letters between the numbers.
def check_letters(cl):
    i = None
    # Sets var for break
    for n in cl:
        if n.isnumeric():
            i = n
            break
    # Splits at i
    cllist = list(cl.split(i, maxsplit = 1))
    if cllist[1].isnumeric():
        #print(debug(8))
        return True
    else:
        #print(debug(9))
        return False





def debug(db):
    match db:
        case 1:
            print("debug 1 - pass - All alphanumeric and correct length ")
        case 2:
            print("debug 2 - fail - The plate is too long or not alphanumeric")
        case 3:
            print("debug 3 - pass - First two characters are letters")
        case 4:
            print("debug 4 - fail - First two characters are not letters")
        case 5:
            print("debug 5 - pass - All letters")
        case 6:
            print("debug 6 - fail - Zero is the first number")
        case 7:
            print("debug 7 - pass - Zero is not the first number pass...")
        case 8:
            print("debug 8 - pass - There are no letters after the first number")
        case 9:
            print("debug 9 - fail - There are letters after the first number")
        case _:
            return None


main()
