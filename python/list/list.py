#def find_largest_smallest(numbers):
    #largest = numbers[0]
    #smallest = numbers[0]
    #for number in numbers:
        #if number > largest:
       #     largest = number
      #  elif number < smallest:
     #       smallest = number
    #return largest, smallest

# Example usage
#numbers = [3, 5, 1, 9, 2, 7]
#largest, smallest = find_largest_smallest(numbers)
#print("Numbers:", numbers)
#print("Largest number:", largest)
#print("Smallest number:", smallest)


def calculate(operand1, operand2, operation): #if-elif-else --> only the action for the first true statement executes
    if operation == 'add':
        return operand1 + operand2
    elif operation == 'subtract':
        return operand1 - operand2
    elif operation == 'multiply':
        return operand1 * operand2
    elif operation == 'divide':
        # check zero division
        if operand2 == 0:
            print('I cannot divide by 0.')
            return None
        return operand1 / operand2

    # invalid operation
    print(f"'{operation}' unknown")
    return None