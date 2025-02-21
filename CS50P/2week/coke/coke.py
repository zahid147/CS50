def main():
    a = 50
    while True:
        print("Amount Due: {}".format(a))
        b = int(input("Insert Coin: "))

        if b == 25 or b == 10 or b == 5:
            a = a - b
        else:
            continue

        if a == 0:
            print("Change Owed: 0")
            exit()
        elif a < 0:
            print("Change Owed: {}".format(abs(a)))
            exit()


main()
