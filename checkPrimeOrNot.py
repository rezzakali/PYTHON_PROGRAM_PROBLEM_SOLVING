num = int(input("Enter the number:"))

for i in range(2, num):
    if num % i == 0:
        print(num, "isn't a prime number.")
        break
else:
    print(num, 'is a prime number.')
