# Convert input, removing vowels


def main():
    user_input = input("Enter your twt: ")
    print(shorten(user_input))


def shorten(word):
    for letter in word:
        match letter:
            case "a":
                word = word.replace("a", "")
            case "A":
                word = word.replace("A", "")
            case "e":
                word = word.replace("e", "")
            case "E":
                word = word.replace("E", "")
            case "o":
               word = word.replace("o", "")
            case "O":
                word = word.replace("O", "")
            case "i":
                word = word.replace("i", "")
            case "I":
                word = word.replace("I", "")
            case "u":
                word = word.replace("u", "")
            case "U":
                word = word.replace("U", "")
    return word


if __name__ == "__main__":
    main()
