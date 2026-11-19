numbers = [5, 12, 8, 20, 12, 7, 30, 5, 15]

"""
Find the sum of all numbers in a list without using sum().



Count how many numbers are greater than 10.



Create a new list containing only even numbers.



Find the duplicate elements in a list.



Find the frequency of a given number.
"""
total = 0
for num in numbers:
    total += num
print(total)

count = 0

for num in numbers:
    if num > 10:
        count += 1

print(count)

evnlist = []

for num in numbers:
    if num % 2  == 0:
        evnlist.append(num)

print(evnlist)

processedList = []
duplicateList = []

for num in numbers:
    if num not in processedList:
        processedList.append(num)
    else:
        duplicateList.append(num)

print(duplicateList)

numbers = [5, 12, 8, 20, 12, 7, 30, 5, 15]

target = 12

count = 0
for num in numbers:
    if num == target:
        count += 1

print(count)