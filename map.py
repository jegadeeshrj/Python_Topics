# 1) Basic Functions
def square(x):
    return x ** 2


numbers = [1, 2, 3, 4, 5]
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
words = ['hello', 'world', 'python']

# MAP with square function to each number
squared_numbers = map(square, numbers)

# MAP object to a LIST
squared_numbers_list = list(squared_numbers)

# Output: [1, 4, 9, 16, 25]
print("Basic Squared Number :", squared_numbers_list)

# 2) Lambda Functions
# MAP with lambda function
squared_numbers = map(lambda x: x ** 2, numbers)

squared_numbers_list = list(squared_numbers)

# Output: [1, 4, 9, 16, 25]
print("Using the Lambda Function :", squared_numbers_list)


# 3) Multiple Iterables
# Function to add two numbers
def add(x, y):
    return x + y


# Using map to apply the add function to pairs of numbers
result = map(add, numbers1, numbers2)

result_list = list(result)

print("Multiple Iterables :", result_list)  # Output: [5, 7, 9]

# 4) Using map() with Strings
# Using map to convert strings to uppercase
uppercase_words = map(str.upper, words)

# Convert to a list
uppercase_list = list(uppercase_words)

print(uppercase_list)  # Output: ['HELLO', 'WORLD', 'PYTHON']
