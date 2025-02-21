def main():
    N = int(input())
    N = str(factorial(N))
    print(N[-4:])

def factorial(n):
	if n == 1:
		return n
	else:
		return n * factorial(n-1)

main()