import inflect
from datetime import date
import re
import sys


def main():
    birthday = date_validation(input("Date of Birth: "))
    if birthday == "Invalid Date":
        sys.exit(birthday)
    else:
        print(f"{quick_maths(birthday)} minutes")

def quick_maths(birthday):
    p = inflect.engine()
    birthday = date.fromisoformat(birthday)
    today = date.today()
    delta_secs = birthday - today
    delta_secs = delta_secs.days * -1 * 24 * 60
    return (p.number_to_words(delta_secs, andword= "").capitalize())

def date_validation(bd):
    pattern = r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
    if re.search(pattern, bd):
        return date_check(bd)
    else:
        return ("Invalid Date")

def date_check(bd):
    bd_sep = bd.split("-")
    bd_year = int(bd_sep[0])
    bd_month = int(bd_sep[1])
    bd_day = int(bd_sep[2])

    try:
        if date(bd_year, bd_month, bd_day):
            return bd
    except ValueError:
        return "Invalid Date"


if __name__ == "__main__":
    main()
