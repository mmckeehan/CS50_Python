import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if re.search(r" - ", s, re.IGNORECASE):
            raise ValueError
    except ValueError:
        raise ValueError

    try:
        s = re.split(r" to ", s)
        time1 = s[0]
        time2 = s[1]

        if re.search(r"[0-9]{1,2} (AM|PM)", time1, re.IGNORECASE):
            time1 = time1.split(" ")
        else:
            raise ValueError
        if re.search(r"[0-9]{1,2} (AM|PM)", time2, re.IGNORECASE):
            time2 = time2.split(" ")
        else:
            raise ValueError

        time1 = convert_time(time1[0], time1[1])
        time2 = convert_time(time2[0], time2[1])

        return f"{time1} to {time2}"
    except ValueError:
        raise ValueError

def convert_time(time, AMPM):
    if re.search(r"[0-9]{1,2}:[0-9]{2}", time):
        time = time.split(":")
        hours = convert_hours(time[0], AMPM)
        minutes = convert_minutes(time[1])
        if minutes == None:
            minutes = 0
        return (f"{hours[0]:02}:{minutes:02}")
    else:
        hours = convert_hours(time, AMPM)
        return (f"{hours[0]:02}:00")
def convert_hours(hour, AMPM):
    hour = int(hour)
    try:
        if AMPM == "AM" and hour == 12:
            hour = hour - 12
        if AMPM == "PM":
            if 0 < hour < 13:
                if hour < 12:
                    hour = hour + 12
            else:
                raise ValueError
        return hour, AMPM
    except ValueError:
        raise ValueError

def convert_minutes(minutes):
    try:
        if 0 <= int(minutes) < 60:
            return minutes
        else:
            raise ValueError
    except ValueError:
        raise ValueError

if __name__ == "__main__":
    main()
