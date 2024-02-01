# upload a file with sample data. This will be done as a command line arugment
    # Can only accept two arugments
    # Second arugment must be a CSV file type.
# Ask for date range
# Return all data within that date range
# select what data is wanting to be tracked
# Return just that data
# Create a graph of the persons choosing based on that data.

import sys
import csv

# This class will handle the CSV.
class Input_CSV():
    ...


def main():
    data_file = correct_args(sys.argv)

    if data_file == None:
        sys.exit("The selected file is not a CSV")

    date_range(data_file)

# Get the desired date range from the user
def date_range(df):
    dates = Input_CSV.date_range(df)

# Checks to see if there are only two command line arugments
def correct_args(df: str):
    if len(df) < 2:
        sys.exit(ValueError("Too Few Arugments"))
    elif len(df) < 2:
        sys.exit(ValueError("Too Few Arugments"))
    else:
        confirm_csv(df[1])
        return df[1]

# Verifies that the second command line arugment is a CSV
def confirm_csv(df: str):
    if df.endswith(".csv"):
        return df
    else:
        return None

if __name__ == "__main__":
    main()