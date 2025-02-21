def main():
    fuel = input("Fraction: ")
    fuel = convert(fuel)
    result = gauge(fuel)
    print(result)


def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() and y.isdigit():
        raise ValueError
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    fraction = (x / y) * 100
    return round(fraction)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
