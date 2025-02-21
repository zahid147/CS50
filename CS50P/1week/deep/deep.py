def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    list = {"42", "forty-two", "forty two"}

    if ans.lower().strip() in list:
        print("Yes")
    else:
        print("No")


main()