def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = filter_even_numbers(numbers)

print(even_numbers)