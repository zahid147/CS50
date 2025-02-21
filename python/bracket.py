text = input()
c1, c2, c3, c4, c5, c6 = 0, 0, 0, 0, 0, 0
for i in text:
	if i == '(':
		c1 += 1
	elif i == ')':
		c2 += 1
		if c1 > 0:
			c1 -= 1
			c2 -= 1

	elif i == '{':
		c3 += 1
	elif i == '}':
		c4 += 1
		if c3 > 0:
			c3 -= 1
			c4 -= 1

	elif i == '[':
		c5 += 1
	elif i == ']':
		c6 += 1
		if c5 > 0:
			c5 -= 1
			c6 -= 1

if (c1+c2+c3+c4+c5+c6) == 0:
	print("Yes")
else:
	print("No")