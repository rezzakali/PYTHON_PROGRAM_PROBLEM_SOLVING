print("Don't enter zero or same numbers:")
firstNumber = int(input("Enter the first number:"))
secondNumber = int(input("Enter the second number:"))
thirdNumber = int(input("Enter the third number:"))

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print(firstNumber, 'is a greatest number.')
elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print(secondNumber, 'is a greatest number.')
else:
    print(thirdNumber, 'is a greatest number.')
