from audioop import reverse
from math import remainder


def isPalindromeNumber(n):
    remainder = 0
    reverse = 0
    while(n != 0):
        remainder = n % 10
        reverse = 10*reverse + remainder
        n = int(n/10)
    return reverse


n = int(input("Enter the number: "))
reverse = isPalindromeNumber(n)
if(reverse == n):
    print(n, " is a palindrome number.")
else:
    print(n, " is not a palindrome number.")
