def main():
    list = ["a", "e", "i", "o", "u"]
    text = input("Input: ")

    print("Output: ", end="")

    for i in text:
        if i.lower() in list:
            print(end="")
        else:
            print(i, end="")

    print()


main()
