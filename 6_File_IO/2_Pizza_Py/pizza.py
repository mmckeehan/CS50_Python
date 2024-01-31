import sys
import csv
import tabulate


def main():
    pizza = pizza_arg()
    pizza = read_csv(pizza)
    tab(pizza)
    #print(pizza)

def pizza_arg():
    try:
        p = sys.argv[1]
        if len(sys.argv) == 2:
            try:
                if p.endswith(".csv"):
                    return sys.argv[1]
                else:
                    print("Not a CSV")
                    sys.exit(1)
            except FileNotFoundError:
                print("File does not exist")
        else:
            print("Invalid arugments.")
            sys.exit(1)
    except IndexError:
        sys.exit("Too Few command-line arugments")

def read_csv(p):
    menue = []
    with open(p, newline='') as csvfile:
        m = csv.DictReader(csvfile)
        for row in m:
            menue.append(row)
    return menue

def tab(t):
    print(tabulate.tabulate(t, headers="keys", tablefmt= "grid"))

if __name__ == "__main__":
    main()
