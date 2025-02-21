import csv
print("How many number do you want to save? ", end="")
n = int(input())
for a in range(n):
    with open("phonebook.csv", "a") as file:
        name = input("Name: ")
        number = input("Number: ")

        writer = csv.writer(file)
        writer.writerow([name, number])