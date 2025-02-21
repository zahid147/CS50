import inflect
p = inflect.engine()

li = []

while True:
    try:
        tmp = input("Name: ")
        li.append(tmp)
    except:
        break

print("Adieu, adieu, to ",end='')
temp = p.join(li)
print(temp)

# tmp = len(li)
# for i in range(tmp):
#     print(li[i],end='')
#     if tmp-i-2 == 0: print(", and ",end='')
#     elif i == tmp-1: continue
#     else: print(', ',end='')
# print()
