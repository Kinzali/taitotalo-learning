# In Python, a list is a collection of items that are ordered and mutable. Each item in a list is separated by a comma and enclosed in square brackets [ ]. 
# Here's an example of how to create a list:
my_list = [1, 2, 3, "four", 5.0]

# create a list of numbers
numbers = [5, 2, 9, 3, 7]
# initialize the smallest value to be the first number in the list
smallest = numbers[0]

# loop through the list to find the smallest value
for num in numbers:
    if num < smallest:
        smallest = num

# print the smallest value
print("The smallest number is:", smallest)


