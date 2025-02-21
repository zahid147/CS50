def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        exit()


def convert(time):
    if " " in time:
        x, y = time.split(":")
        y, z = y.split(" ")
        x, y = int(x), int(y)
        y = y / 60
        if z == "a.m.":
            t = x + y
        elif z == "p.m.":
            t = 12 + x + y
        return t

    else:
        x, y = time.split(":")
        x, y = int(x), int(y)
        y = y / 60
        z = x + y
        return z


if __name__ == "__main__":
    main()
