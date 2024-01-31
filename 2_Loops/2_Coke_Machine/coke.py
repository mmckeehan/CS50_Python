# print ammount due (total)
# ask for input
# Subtract input from total
# IF total < input then ask for more money
# IF total > input, RETURN the remainder

def main ():
    cost = 50
    math(cost)

def math (total):
    while total <= 50 and total > 0:
        print (f"Amount Due: {total}")
        payment = input("Insert Coins: ")
        total = total - pay(int(payment))
        if total <= 0:
            change = total * -1
            print(f"Change Owed: {change}")

def pay (p):
    if p == 1:
        return p
    elif p == 5:
        return p
    elif p == 10:
        return p
    elif p == 25:
        return p
    elif p == 50:
        return p
    else:
        return 0

main()
