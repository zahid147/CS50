def main():
    text = input("Greeting: ")
    x  = value(text)
    print(f"${x}")


def value(greeting):
    if 'Hello' in greeting:
        return 0
    if 'H' in greeting:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
