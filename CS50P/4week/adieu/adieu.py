import inflect

p = inflect.engine()

list = []
while True:
    try:
        text = input("Name: ")
        list.append(text)
    except EOFError:
        print()
        break

output = p.join(list)
print("Adieu, adieu, to", output)