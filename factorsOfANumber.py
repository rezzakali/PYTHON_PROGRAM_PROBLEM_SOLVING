number = int(input("Enter the number:"))

print("The factor of {} are ".format(number))

for i in range(1, number+1):
    if number % i == 0:
        print(i)
