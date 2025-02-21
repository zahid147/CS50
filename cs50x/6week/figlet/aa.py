import cs50
from pyfiglet import Figlet
import sys

figlet = Figlet()
n = len(sys.argv)
fonts = figlet.getFonts()

print(fonts)