def main():
    greeting = input(("Greeting: ").strip().lower())
    print(value(greeting))

def value(greeting):
     # if Hello - $0
    if greeting.startswith("h"):
        if greeting == "hello":
            return 0
        else:
            return 20
    # else $100
    else:
        return 100

if __name__ == "__main__":
    main()
