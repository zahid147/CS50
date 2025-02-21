for _ in range(int(input())):
    n,m = map(int,input().split())
    if m > n: print("No")
    elif m == n: print("Yes")
    elif m%2 == 0:
        if n%2 == 0: print("Yes")
        else: print("No")
    elif m%2 != 0:
        if n%2 != 0: print("Yes")
        else: print("No")
