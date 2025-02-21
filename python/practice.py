case = int(input())
for i in range(case):
        N = int(input())
        A, B = map(int, input().split())
        list = map(int, input().split())
        count = 0

        for j in range(N-1):
                for k in range(j+1,N):
                        if A <= (list[j] + list[k]) <= B:
                                count += 1
        print(f"Case {i+1}: {count}")