list = []
counter = {}

while True:
    try:
        item = input()
        list.append(item.lower())
    except EOFError:
        print()
        break

for item in list:
    if item not in counter:
        counter[item] = 0
    counter[item] += 1

for item in sorted(counter):
    print(f"{counter[item]} {item.upper()}")
