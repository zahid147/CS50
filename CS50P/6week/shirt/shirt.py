import sys
from PIL import Image, ImageOps

def main():
    check_command_line()

    try:
        image = Image.open(sys.argv[1])
    except:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    background = ImageOps.fit(image, size)
    background.paste(shirt, shirt)
    background.save(sys.argv[2])



def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    extention = ['png', 'jpg', 'jpeg']
    temp1 = sys.argv[1].split(".")
    temp2 = sys.argv[2].split(".")

    if temp2[1].lower() not in extention:
        sys.exit("Invalid output")

    if not temp1[1].lower() == temp2[1].lower():
        sys.exit("Input and output have different extensions")

main()