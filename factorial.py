def myFactorial(n):
    fact = 1

    for i in range(n, 0, -1):
        fact = fact * i

    return fact


n = int(input("Enter the number:"))

res = myFactorial(n)
print(res)
