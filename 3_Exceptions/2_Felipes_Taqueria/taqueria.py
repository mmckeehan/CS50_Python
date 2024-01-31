# Create Menue
# Gather input - Case Insensitivity
# Save input in a list
# Repeat until the user hits ctrl-d
# Add the total of the list and return the value

def main():
    menu = {
        'baja taco': 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
        }

    order = []
    while True:
        try:
            order.append(add_item(menu))
        except EOFError:
            break
        total = "{:.2f}".format((sum(order)))
        print(f"${total}")

def add_item(d):
    i_bool = False
    while i_bool == False:
        item = input("Item: ").lower()
        try:
            return(d[item])
            i_bool = True
        except KeyError:
            i_bool = False










main()
