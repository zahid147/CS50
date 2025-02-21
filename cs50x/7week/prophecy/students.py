import csv
from cs50 import SQL


def main():
    db = SQL("sqlite:///roster.db")

    students = []
    houses = []
    relation = []

    with open("students.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["student_name"]
            house = row["house"]
            head = row["head"]

            create_house(house, houses, head)
            create_student(name, students)
            create_relation(name, house, relation)

    for student in students:
        db.execute(
            "INSERT INTO new_students (student_name) VALUES (?)",
            student["student_name"],
        )

    for rel in relation:
        db.execute(
            "INSERT INTO relation (student_name, house) VALUES (?,?)",
            rel["student_name"],
            rel["house"],
        )

    for house in houses:
        db.execute(
            "INSERT INTO houses (house, head) VALUES (?,?)",
            house["house"],
            house["head"],
        )


def create_house(house, houses, head):
    count = 0
    for h in houses:
        if h["house"] == house:
            count += 1
    if count == 0:
        houses.append({"house": house, "head": head})


def create_student(name, students):
    students.append({"student_name": name})


def create_relation(name, house, relation):
    relation.append({"student_name": name, "house": house})

if __name__ == "__main__":
    main()