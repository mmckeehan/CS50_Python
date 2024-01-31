import sys
import requests
import json


def main():
    bit_coin = initial_input()

    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = r.json()
    bpi_dict = o["bpi"]
    USD_dict = bpi_dict["USD"]
    rf = USD_dict["rate_float"]
    rf = float(rf)

    value = get_value(bit_coin, rf)
    print(f"${value}")


def initial_input():
    # Provides initial value for the Bitcoin amount from arugment passed through CLI
    if len(sys.argv) == 2:
        bc = sys.argv[1]
        try:
            bc = float(bc)
            return bc
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        if len(sys.argv) <= 1:
            print("Missing command-line argument")
            sys.exit(1)


def get_value(bc_value, rf_value):
    final_value = round(bc_value * rf_value, 4)
    final_value = f"{final_value:,}"
    return final_value


main()
