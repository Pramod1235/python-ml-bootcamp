## Linear search in a list

numbers = [12, 5, 28, 7, 19, 3, 45, 10, 2]
findNumber = 19

for i in range(len(numbers)):

    print(numbers[i])
    if (numbers[i] == findNumber):
        print(i)
