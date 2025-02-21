def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    n = len(plate)
    list = []

    if n not in range(2,7):
        return False

    if plate[0].isalpha() and plate[1].isalpha():
        x = 0
    else:
        return False

    for i in range(n):
        if plate[i].isalpha() or plate[i].isdigit():
            x = 0
        else:
            return False

        if plate[i].isdigit():
            for j in range(i, n):
                if plate[j].isalpha():
                    return False

    for i in plate:
        if i.isdigit():
            list.append(i)

    if len(list) != 0:
        if list[0] == "0":
            return False

    return True


if __name__ == "__main__":
    main()
