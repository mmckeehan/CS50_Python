def main():
    # Get Input of time in format #:## or ##:##
    t = convert(input("What time is it: ").strip())

    # Determine IF the time falls within one of the meal times. Let the user know what meal that they should be eating.

    if 7.0 <= t <= 8.0:
        print ("breakfast time")
    elif 12 <= t <= 13:
        print ("lunch time")
    elif 18 <= t <= 19:
        print ("dinner time")
    #print(t)

def convert(time):
    # CONVERT the time to a readable input
    # Convert enetered time from ##:## to ##.##
    time = time.split(":")
    time1 = float(time[0])
    time2 = float(time[1])
    time2 = float(time2 / 60)

    return time1 + time2



if __name__ == "__main__":
    main()
