import sys
import csv

def main():
    new(import_before())
    #new("before.csv")

def import_before():
    # Import exactly two arugments
    try:
        before_csv = sys.argv[1]
        if len(sys.argv) == 3:
            is_csv(before_csv)
            return before_csv
        elif len(sys.argv) == 2:
            print("Too few command-line arguments")
            sys.exit(1)
        else:
            print("Too many command-line arguments")
            sys.exit(1)
    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)

def is_csv(csv):
    #Check to ensure that the file is a csv
    if csv.endswith(".csv"):
        return csv
    else:
        print(f"Could not read {csv}")
        sys.exit(1)

def new(unclean):
    clean = correct_csv(import_csv(unclean))
    new_file_name = sys.argv[2]
    field_names = ["first", "last", "house"]
    # Will need to create a new CSV with filename sys.argv[2]
    with open(new_file_name, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(clean)

def import_csv(unclean):
    # This function is get the file ready to be corrected.
    to_clean = []
    with open(unclean, newline="") as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            to_clean.append(row)
    return to_clean

def correct_csv(to_clean):
    # This function is used to separate the "name" for each user and swap them
    new_dict = []
    to_clean = list(to_clean)
    for clean in to_clean:
        clean_n = clean["name"]
        clean_n = clean_n.split(", ")
        new_dict.append(
        {
        "first": clean_n[1].strip(),
        "last": clean_n[0],
        "house": clean["house"]
        })
    return new_dict




if __name__ == "__main__":
    main()
