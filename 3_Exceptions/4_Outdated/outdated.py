# Get Input of either 'DD Month, YYYY' OR 'DD/MM/YYYY'
# VALIDATE that there is no more than 31 days
# CONVERT to a format YYYY-MM-DD

def main ():

    user_input = v_input_mide(input("Date: ").lower().strip())
    print(user_input)

def v_input_mide(date):
    if "/" in date:# and date.find("/") == 2:
        date = date.split("/")

        try:
            if 1 <= int(date[0]) <= 12 and 1 <= int(date[1]) <= 31:
                date[0] = add_zero(date[0])
                date[1] = add_zero(date[1])
                return (f"{date[2]}-{date[0]}-{date[1]}")
            else:
                main()
        except ValueError:
            main()

    else:
        test = v_input_type(date)
        return test



def v_input_type(date):
    month = {
    "january" : "01",
    "february" : "02",
    "march" : "03",
    "april" : "04",
    "may" : "05",
    "june" : "06",
    "july" : "07",
    "august": "08",
    "september" : "09",
    "october" : "10",
    "november" : "11",
    "december" : "12"
    }

    date.lower()

    if "," in date:
        date = date.split(" ")
        date[1] = date[1].removesuffix(",")

        try:
            month[date[0]]
        except KeyError:
            main()

        if 1 <= int(date[1]) <= 31:
            date[1] = str(date[1].zfill(2))
            date = (f"{date[2]}-{month[date[0]]}-{date[1]}")
            return date
        else:
            main()

    else:
        main()

def add_zero(num):
    if num.count == 2:
        return num
    else:
        return num.zfill(2)


main()
