number = int(input("Enter the number:"))
m = len(str(number))
temp = number
sum = 0
while temp != 0:
    remainder = temp % 10
    sum = sum + remainder**m
    temp = temp//10
if sum == number:
    print(sum, 'is a armstrong number.')
else:
    print(sum, 'is not a armstrong number')
