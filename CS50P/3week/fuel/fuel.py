def main():
    while True:
        fuel = input("Fraction: ")

        try:
            x, y = fuel.split("/")
            x, y = int(x), int(y)
            f = (x / y) * 100
            if f <= 100:
                break
        except (ValueError, ZeroDivisionError):
            pass

    if f <= 1:
        print("E")
    elif 99 <= f <= 100:
        print("F")
    else:
        print(f"{f:.0f}%")


main()
