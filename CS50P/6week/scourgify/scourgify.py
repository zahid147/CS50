import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

list = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
             temp = row["name"].split(", ")
             list.append({"first": temp[1], "last": temp[0], "house": row['house']})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": 'first', "last": 'last', "house": 'house'})
        for row in list:
             writer.writerow({"first": row['first'], "last": row['last'], "house": row['house']})


except FileNotFoundError:
    sys.exit("File does not exist")
