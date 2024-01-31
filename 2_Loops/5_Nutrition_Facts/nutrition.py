def main():
    user_input = input("Item: ").lower()
    fruit_dict(user_input)



def fruit_dict(ui):
    #debug(2, ui)
    # Create dictionary
    fdict = {
        "Fruit Name": "Calories",
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": 90,
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "Strawberries": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80",
    }
    # Iterate through dict to find fruit
    for f in fdict:
        if f == ui:
            #debug(1)
            print (f"Calories: {fdict[f]}")

    # return calories for the fruit


def debug(db, *ui):
    match db:
        case 1:
            print("debug 1 - pass - Calories are being found")
        case 2:
            print(f"debug 2 - pass - User input was accepted... {ui}")
        case _: return None

main()
