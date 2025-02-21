def main():
    text = input("camelCase: ")

    print("snake_case: ", end="")

    for i in text:
        if i.isupper():
            print("_{}".format(i.lower()), end="")
        else:
            print(i, end="")
    print()


main()
