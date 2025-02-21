num = int(input())
if num == 1:
    print("No")
    exit()
for i in range(2,num):
    if num%i == 0:
        print("No")
        exit()
print("Yes")
