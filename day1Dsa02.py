numbers = [12, 5, 28, 7, 19, 3, 45, 10, 2]

max = numbers[0]

for i in range(len(numbers)):

    if (numbers[i] > max):
        max = numbers[i]

print(max)

min = numbers[0]

for i in range(len(numbers)):
    if(numbers[i] < min):
        min = numbers[i]

print(min)