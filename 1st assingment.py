# Exercise 1

def multiply_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Example usage:
num1 = 20
num2 = 50
result = multiply_or_sum(num1, num2)
print("Result:", result)

# Exercise 2:

def sum_previous_and_current(numbers):
    result = []
    previous_number = None
    for current_number in numbers:
        if previous_number is not None:
            result.append(previous_number + current_number)
        previous_number = current_number
    return result

# Iterate over the first 10 numbers
for i in range(1, 11):
    numbers = list(range(i))
    sums = sum_previous_and_current(numbers)
    print(f"Numbers: {numbers}, Sums: {sums}")

# Exercise 3:

# Accepting a string from the user
user_string = input("Enter a string: ")

# Displaying characters present at even index numbers
even_index_characters = user_string[::2]
print("Characters at even index numbers:", even_index_characters)

# Exercise 4:

def remove_chars(string, n):
    return string[n:]

# Example usage
input_string = "pynative"
n = 4
result = remove_chars(input_string, n)
print("Result:", result)

# Exercise 5:

def check_first_last_same(numbers):
    if len(numbers) < 2:
        return "List is too short to compare first and last numbers."
    elif numbers[0] == numbers[-1]:
        return "First and last numbers are same."
    else:
        return "First and last numbers are not same."

# Example usage
input_list = [1, 2, 3, 4, 1]
result = check_first_last_same(input_list)
print(result)

# Exercise 6:

def display_divisible_by_5(numbers):
    divisible_by_5 = [num for num in numbers if num % 5 == 0]
    print("Numbers divisible by 5:", divisible_by_5)

# Example usage
input_list = [10, 25, 36, 45, 50, 63]
display_divisible_by_5(input_list)

# Exercise 7:

def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Number of rows in the pattern
rows = 5
print_pattern(rows)

# Exercise 8:

def is_palindrome_number(number):
    # Convert the number to a string for easier manipulation
    number_str = str(number)
    # Check if the number is equal to its reverse
    return number_str == number_str[::-1]

# Example usage
input_number = 545
if is_palindrome_number(input_number):
    print(f"{input_number} is a palindrome number.")
else:
    print(f"{input_number} is not a palindrome number.")

# Exercise 9:

def create_new_list(list1, list2):
    new_list = []
    # Add odd numbers from the first list
    for num in list1:
        if num % 2 != 0:
            new_list.append(num)
    # Add even numbers from the second list
    for num in list2:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

# Example lists
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

# Create a new list based on the condition
result_list = create_new_list(list1, list2)
print("New list:", result_list)

# Exercise 10:

def extract_digits_reverse(number):
    # Convert the number to a string
    number_str = str(number)
    # Extract each digit in reverse order and print with space separator
    for digit in reversed(number_str):
        print(digit, end=" ")

# Example usage
input_number = 7536
print("Output:", end=" ")
extract_digits_reverse(input_number)

