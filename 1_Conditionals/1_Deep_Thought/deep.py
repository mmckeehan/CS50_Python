def main():
    ans = input("What is the meaning of life? ")

    match ans.lower().strip():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")



main()
