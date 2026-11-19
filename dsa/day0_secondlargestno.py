numbers = [2, 7, 11, 15, 3, 9, 20]

"""
Find how many times 3 appears.

Expected output: 1

Problem 2: Find second-largest number

Expected output: 15

Rules:
- Don't use count().
- Don't use sort().
- Don't use max() or min().
"""

count = 0

for num in numbers:

    if num == 3:
        count += 1

print(count)

numbers1 = [2, 7, 20, 15, 20, 9]

max = numbers1[0]
secondlargest = numbers1[0]
# Find second largest no

for num in numbers1:
    if num > max:
        secondlargest = max
        max = num
    elif max > num > secondlargest:
        secondlargest = num

print(secondlargest)
