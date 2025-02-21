from cs50 import get_float


def main():
    # Ask how many cents the customer is owed
    while True:
        total = get_float("Change owed: ")
        if total > 0:
            break
    cents = int(total * 100)

    # Calculate the number of quarters to give the customer
    quarters = c_quarters(cents)
    cents = cents - quarters * 25

    # Calculate the number of dimes to give the customer
    dimes = c_dimes(cents)
    cents = cents - dimes * 10

    # Calculate the number of nickels to give the customer
    nickels = c_nickels(cents)
    cents = cents - nickels * 5

    # Calculate the number of pennies to give the customer
    pennies = cents

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Prtotal number of coins to give the customer
    print(coins)


def c_quarters(cents):
    quarter = 25
    total = cents
    q = 0
    while True:
        if total >= quarter:
            total = total - quarter
            q += 1
        elif total < quarter:
            break
    return q


def c_dimes(cents):
    dime = 10
    total = cents
    d = 0
    while True:
        if total >= dime:
            total = total - dime
            d += 1
        elif total < dime:
            break
    return d


def c_nickels(cents):
    nickel = 5
    total = cents
    n = 0
    while True:
        if total >= nickel:
            total = total - nickel
            n += 1
        elif total < nickel:
            break
    return n


if __name__ == "__main__":
    main()