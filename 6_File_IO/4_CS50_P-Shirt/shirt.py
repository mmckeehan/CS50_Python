import sys
from PIL import Image
from PIL import ImageOps
from os.path import splitext


def main():
    cla()
    img_convert()


def cla():
    input = sys.argv[1]
    output = sys.argv[2]
    # if the user does not specify exactly two command-line arguments,
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    check_file_type(input, output)
    # if the specified input does not exist.
    try:
        Image.open(input)
    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_file_type(input, output):
    # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    # if the input’s name does not have the same extension as the output’s name
    new_input = splitext(input)
    input_file_type = new_input[1]
    new_output = splitext(output)
    output_file_type = new_output[1]

    if input_file_type in (".jpeg", ".jpg", ".png"):
        if input_file_type in (".jpeg", ".jpg", ".png"):
            if input_file_type.lower() == output_file_type.lower():
                return input, output
            else:
                sys.exit("Input and output have different extensions")
        else:
           sys.exit("Invalid output")
    else:
        sys.exit("Invalid input")





def img_convert():
    shirt = Image.open("shirt.png")
    size = shirt.size
    user = Image.open(str(sys.argv[1]))
    new_image = str(sys.argv[2])
    user = ImageOps.fit(user, size)
    user.paste(shirt, shirt)
    user.save(new_image)

if __name__ == "__main__":
    main()
