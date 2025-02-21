def main():
    x, y, z = input("Enter three values: ").split()
    x, z = int(x), int(z)

    if y == "+":
        math = x + z
    elif y == "-":
        math = x - z
    elif y == "*":
        math = x * z
    elif y == "/":
        math = x / z

    print(f"{math:.1f}")


main()
