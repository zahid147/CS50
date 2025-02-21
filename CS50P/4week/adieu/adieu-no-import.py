list = []
while True:
    try:
        text = input("Name: ")
        list.append(text)
    except EOFError:
        print()
        break

n = len(list)
if n < 1:
    exit()
print("Adieu, adieu, to ", end="")
if n == 1:
    print(list[0])
elif n == 2:
    print(list[0], "and", list[1])
else:
    for name in range(n - 1):
        print(list[name] + ", ", end="")
    print("and", list[n - 1])
