list = ['0','1','2','3','4','5','6','O']

N = int(input())

for i in range(N):
    text = input()
    count = 0

    for i in text:
        if i in list:
            count += 1

    over = int(count / 6)
    ball = count % 6

    if over > 0 and ball == 0:
        if over > 1:
            print(over, "OVERS")
        else:
            print(over, "OVER")

    elif ball > 0 and over == 0:
        if ball > 1:
            print(ball, "BALLS")
        else:
            print(ball, "BALL")

    else:
        if ball > 1 and over > 1:
            print(over, "OVERS", ball, "BALLS")
        elif ball > 1 and over == 1:
            print(over, "OVER", ball, "BALLS")
        elif ball == 1 and over > 1:
            print(over, "OVERS", ball, "BALL")
        elif ball == 1 and over == 1:
            print(over, "OVER", ball, "BALL")