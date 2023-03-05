def find_largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number
    return largest, smallest

# Example usage
numbers = [3, 5, 1, 9, 2, 7]
largest, smallest = find_largest_smallest(numbers)
print("Numbers:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
