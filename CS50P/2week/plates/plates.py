def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    n = len(plate)
    b = True
    list = []

    if not 2 <= n <= 6:
        return False

    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    for i in range(2,n):
        if not plate[i].isalnum():
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


    return b


if __name__ == "__main__":
    main()
