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

#pythonfuntions:

#calling a function
def my_function():
    print("hello this is kinza: ")
my_function()
    

#arguments in functions: #arguments are also called args 
#parameters and arguments are used for the same thing.
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#number of arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#arbiterary arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


#keywords arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#arbitrary keyword arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#default parameter value:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

