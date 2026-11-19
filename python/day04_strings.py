text = "artificial intelligence"

"""
Write these five programs:
1. Reverse a string without using [::-1].
2. Check whether a string is a palindrome.
3. Count vowels in a string.
4. Count the number of words in a sentence.
5. Find the first non-repeating character.
"""

def reverse_string(s):
    return s[::-1]

def reverse_string_(s):
    reversed_string = ""
    for i in range(len(s)-1, -1, -1):
        reversed_string += "".join(s[i])
    print(reversed_string)
    return reversed_string


print(reverse_string_(text))

def checkPalindrome(s):
    if reverse_string_(s) == s:
        return "Palindrome"
    else:
        return False

def checkPalindrome2(s):

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return "Palindrome"

print(checkPalindrome2("madam"))
print(checkPalindrome2("madam"))


def countVowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count

print(countVowels("madam"))

count = sum(1 for ch in "madam" if ch in "aeiouAEIOU")

def findnonrepeating(s):

    for i in range(len(s)):

        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return s[i]
        return -1



print(findnonrepeating("madam"))