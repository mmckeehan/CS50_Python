def main():
    # take in input
    # trim the input to get rid of leading/ trailing spaces
    # split the string based on ' '
    userInput = input("x [operator] y:").strip().split(" ")

    # str1 = first num, str 2 = oper, str 3 = second num
    x = float(userInput[0])
    y = userInput[1]
    z = float(userInput[2])

# perform operation
    # if z = 0, error
    #if z == 0 and y == "/":
     #   print("Error: This is not a valid operation")

    match userInput[1]:
        case "+":
            a = x + z
            print(a)
        case "-":
            a = x - z
            print(a)
        case "*" | "x":
            a = x * z
            print(a)
        case "/":
            if z == 0 and y == "/":
                print("Error: This is not a valid operation")
            else:
                a = x / z
                print(a)






main()
