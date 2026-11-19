numbers = [2, 7, 11, 15]

for i in range(len(numbers)):

    for j in range(i+1, len(numbers)):
        print(numbers[i], numbers[j])

numbers = [1, 5, 7, -1, 5]
target = 6

for i in range(len(numbers)):

    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])