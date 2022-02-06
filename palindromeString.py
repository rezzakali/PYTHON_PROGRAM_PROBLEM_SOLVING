from audioop import reverse


def checkPalindrome(s):
    reverse = s[::-1]
    if(reverse == s):
        print("Yes, it's a palindrome string.")
    else:
        print("Not a palindrome string.")


s = input("Enter the string: ")

checkPalindrome(s)
