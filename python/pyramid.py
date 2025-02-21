height = int(input())

for row in range(0, height):
    for space in range(height, row + 1, -1):
        print(" ", end="")
    for column in range(row + 1):
        if column == 0:
            print("*", end="")
        else:
            print(" *", end="")
    print()