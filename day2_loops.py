## Loops


fruits = ["Apple" , "Banana" , "Orange" , "Grapefruit"]

## Basic for loop
for fruit in fruits:
    print(fruit)


for index , fruit in enumerate(fruits):
    print(index)
    print(fruit)

for i in range(5):
    print(i)

for i in range(0,11,1):
    print(i)

rates = ["100" , "80" , "100" , "150"]

for fruit , rate in zip(fruits , rates):
    print(fruit , rate)

dict = {"apple" : 100 , "orange" : 100 , "grapefruit" : 150 , "banana" : 80 }

for fruit , rate in dict.items():
    print(fruit , rate)

names = "Pramod iNavish"

for ch in names:
    print(ch)


numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:

    if num == 3:
        continue
    if num == 7:
        break
    print(num)

for num in numbers:
    pass
else:
    print('printing completed')

# Nested loops

for num in numbers:

    for i in range(num,11):
        print(i)