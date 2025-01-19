def isAscending(items):
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True
# numbers = [1, 2, 5, 4]
# print(isAscending(numbers))

#################################################
list1 = [1, 17, 29, 23, 12, 4, 13, 2, 7, 9, 8]

def bubbleSort(numbers):
    for i in range(len(numbers) - 1): 
        for j in range(len(numbers) - 1 - i): 
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

print(bubbleSort(list1))
