import cs50
from pyfiglet import Figlet
import sys

figlet = Figlet()
n = len(sys.argv)
fonts = figlet.getFonts()

if sys.argv[1] == "-f":
    correct = True
elif  sys.argv[1] == "--font":
    correct = True
else:
    correct = False

if n > 1 and n < 4:

    if correct == False:
        print("Invalid usage")
        sys.exit(1)

    if sys.argv[2] not in fonts:
        print("Invalid usage")
        sys.exit(2)

    figlet.setFont(font=sys.argv[2])


x = cs50.get_string("Input: ")

print("Output:")
print(figlet.renderText(x))