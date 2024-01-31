# Convert input, removing vowels

def main ():
    usr_input = input("Enter your twt: ")
    convert(usr_input)

def convert(c):
    for l in c:
        print (remove(l), end = "")

    print()

def remove (r):
    match r:
        case "a":
            return r.replace("a", "")
        case "A":
            return r.replace("A", "")
        case "e":
            return r.replace("e", "")
        case "E":
            return r.replace("E", "")
        case "o":
            return r.replace("o", "")
        case "O":
            return r.replace("O", "")
        case "i":
            return r.replace("i", "")
        case "I":
            return r.replace("I", "")
        case "u":
            return r.replace("u", "")
        case "U":
            return r.replace("U", "")
        case _:
            return r

main()
