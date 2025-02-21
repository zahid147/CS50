def main():
    text = input("Input: ")
    text = shorten(text)
    print("Output:", text)


def shorten(word):
    list = ["a", "e", "i", "o", "u"]
    for i in word:
        if i.lower() in list:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
