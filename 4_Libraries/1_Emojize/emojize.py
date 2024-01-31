import emoji

# Propmt for "INPUT"
# Convert that into an Emoji based on 'carpedm20.github.io/emoji/all.html?enableList=enable_list_alias'


def main():
    user_input = input("Input: ")
    print(emoji.emojize(user_input, language='alias'))


if __name__ == "__main__":
    main()
