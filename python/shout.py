text = input().split(" ")
new = list()
for word in text:
	if not word.isupper():
		new.append(word)
print(*new)