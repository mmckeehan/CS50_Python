    # get input for x/y. MUST be numbers and Y != 0.
    # IF above conditions == FALSE, re-prompt.
# return a percentage rounded to the nearest interger
# IF percentage is 1% or less, print "E"

def main():
    fract = fraction(u_input())
    percent(fract)

def percent(p):
    p = round(float(p*100))
    if p >= 99:
        print("F")
    elif 99 > p > 1:
        print(f"{p}%")
    else:
        print("E")

def u_input():
    wbool = True
    while wbool == True:
        user_input = input("Fraction: ")

        if '/' in user_input:
            wbool = False
            return user_input
        else:
            print("Please Enter a fraction")

def fraction(ui):
    while True:
        ui = ui.split("/")

        x = valid_num(ui[0])
        y = valid_num(ui[1])

        if x == 0:
            return 0
        else:
            return maths(x, y)

def maths(x, y):
        try:
            z = x/y
            if z > 1:
                main()
            else:
                return z
        except ZeroDivisionError:
            main()


def valid_num(i):
    try:
        return int(i)
    except ValueError:
        main()


main()
