numbers = [1, 2, 4, 6, 8, 9, 11]
target = 10

"""
Pair Sum in a Sorted Array
"""

def pairSum(numbers):

    for i in range(len(numbers)):

        for j in range(i+1 , len(numbers)):
            if numbers[i] + numbers[j] == target:
                print(f"{numbers[i]} + {numbers[j]} = {target}")

pairSum(numbers)

def reverseAnArray(s):
    reversed_array = []
    for i in range(len(s)-1,-1,-1):
        reversed_array.append(s[i])
    return reversed_array

print(reverseAnArray(numbers))
