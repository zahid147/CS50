list = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

while True:
    text = input()
    text = text.lower()
    for month in list:
        if month == text:
            index = list.index(text) + 1
            print(index)
