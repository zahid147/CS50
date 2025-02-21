from datetime import datetime, date
import inflect
import re
import sys

def main():
    date_of_birth = input("Date of Birth: ")
    text = func(date_of_birth)
    print(text, "minutes")

def func(dob):
    p = inflect.engine()
    match = re.search(r"^\d\d\d\d-\d\d-\d\d$", dob)
    if match:
        dob = datetime.strptime(dob, "%Y-%m-%d")
    else:
        sys.exit("Invalid date")
    current = datetime.strptime(str(date.today()), "%Y-%m-%d")
    delta = current - dob
    minutes = delta.days * 24 * 60
    word = p.number_to_words(minutes, andword="")
    return f"{word.capitalize()}"


if __name__ == "__main__":
    main()
