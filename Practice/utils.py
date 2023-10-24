def find_max(numbers):
    largest_number = numbers[0]

    for index in numbers:
        if index > largest_number:
            largest_number = index

    return largest_number