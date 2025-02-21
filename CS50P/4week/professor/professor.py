from random import randint


def main():
    x = get_level()
    score = 0
    for stage in range(10):
        a, b = generate_integer(x), generate_integer(x)
        sum = a + b
        count = 0
        while True:
            ans = int(input(f"{a} + {b} = "))
            if ans == sum:
                score += 1
                break
            else:
                print("EEE")
                count += 1
                if count == 3:
                    print(f"{a} + {b} = {sum}")
                    break
                pass
    print(score)


def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        number = randint(0, 9)
    elif level == 2:
        number = randint(10, 99)
    elif level == 3:
        number = randint(100, 999)
    else:
        raise ValueError
    return number


if __name__ == "__main__":
    main()
