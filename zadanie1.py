alll = int(input())
numbers = []
for i in range(alll):
    numb = int(input())
    numbers.append(numb)
numbers.sort()
print(numbers)
print(numbers[0])
print(list(reversed(numbers))[0])
