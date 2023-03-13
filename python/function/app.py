def factorial(n):
    """
    This program defines a function called factorial that 
    takes an integer n as input and returns the factorial of that number using recursion.
    The base case of the recursion is when n is 0, in which case the function returns 1.
    Otherwise, the function multiplies n by the result of calling itself with n-1 as the argument,
    which eventually reaches the base case.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
num = 5
print(f"The factorial of {num} is {factorial(num)}")

import re

def word_frequency(text):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    # Split the text into words
    words = text.split()
    # Initialize a dictionary to store the frequency of each word
    freq = {}
    # Count the frequency of each word
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# Test the function
text = "The quick brown fox jumps over the lazy dog. The dog barks at the fox."
freq = word_frequency(text)
print(freq)


