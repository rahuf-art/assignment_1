# Define a list of numbers
numbers = [1, 40, 27, 88, 9, 241, 361, 99, 1001, 53]

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Iterate through the list of numbers and count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display the results
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
