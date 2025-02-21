import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    count = 0
    with open(sys.argv[1]) as file:
        for row in file:
            row = row.lstrip()
            if len(row) > 0:
                if not row.startswith("#"):
                    count += 1
    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
