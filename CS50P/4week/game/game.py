from random import randint

while True:
    try:
        a = input("Level: ")
        a = int(a)
        if a < 1:
            continue
        break
    except ValueError:
        pass
    except EOFError:
        print()
        exit()

ans = randint(1, a)

while True:
    try:
        x = input("Guess: ")
        x = int(x)
        if x < 1:
            continue
        if x > ans:
            print("Too large!")
            continue
        elif x < ans:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break
    except ValueError:
        pass
    except EOFError:
        print()
        exit()
