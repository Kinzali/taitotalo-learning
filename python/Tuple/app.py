# define a function that takes in a list of tuples and returns a new list of tuples
# where each tuple contains the first and last element from each tuple in the original list

def first_last_tuples(tuples_list):
    new_list = []
    for tup in tuples_list:
        first_element = tup[0]
        last_element = tup[-1]
        new_tup = (first_element, last_element)
        new_list.append(new_tup)
    return new_list

# example usage
tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_list = first_last_tuples(tuples_list)
print(new_list)
# output: [(1, 3), (4, 6), (7, 9)]

# define a function that takes in a dictionary and returns a tuple
# containing the key with the highest value and the corresponding value

def max_dict_value(dictionary):
    max_key = None
    max_value = float('-inf')
    for key, value in dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    return (max_key, max_value)

# example usage
my_dict = {'a': 10, 'b': 20, 'c': 30}
max_tuple = max_dict_value(my_dict)
print(max_tuple)
# output: ('c', 30)
