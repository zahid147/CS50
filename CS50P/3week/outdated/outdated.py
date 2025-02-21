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
    text = input("Date: ")
    text = text.lower().strip()

    if "/" in text:
        month, day, year = text.split("/")
        if not month.isdigit() and day.isdigit() and year.isdigit:
            continue
        if int(day) > 31 or int(month) > 12:
            continue
        break

    elif "," in text:
        text, day, year = text.split(" ")
        if not text.isalpha():
            continue
        for month in list:
            if month == text:
                index = list.index(text) + 1
        month = str(index)

        day = day.replace(",", "")
        if int(day) > 31 or int(month) > 12:
            continue
        break

    else:
        continue

print(f"{year.zfill(4)}-{month.zfill(2)}-{day.zfill(2)}")
