from utils import find_max

numbers = []

for number in range(5):
    numbers.append(int(input('Input number: ')))

output = find_max(numbers)

print(f'The largest number is {output}')