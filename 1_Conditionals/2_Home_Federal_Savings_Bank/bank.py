def main():
    # Greet
    greeting = input("Greeting: ").strip().lower()
    # if Hello - $0
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            print ("$0")
        else:
            print ("$20")
    # else $100
    else:
        print ("$100")

main()
