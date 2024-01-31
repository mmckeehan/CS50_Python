import sys

def main():
    user_input = input()
    print(gauge(convert(user_input)))


def convert(fraction):
    # Determine if fraction
    div_bool = True
    while div_bool == True:
        if "/" in fraction:
            div_bool == False
        else:
            raise ValueError

        # Split fraction
        fraction = fraction.split("/")
        x = int(fraction[0])
        y = int(fraction[1])


        # Zero Division Check
        if y <= 0:
            raise ZeroDivisionError
        # x > y Check
        if x > y:
            raise ValueError
        return round((x / y) * 100)


def gauge(percentage):
    # Print percentage
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
