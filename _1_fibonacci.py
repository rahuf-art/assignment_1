# Initialize the first two Fibonacci numbers
a=1
b=0

# Print the initial values (0 and 1)
print(a)

# Generate Fibonacci numbers until reaching 50
while b <= 50:
    print(b)
    a, b = b, a + b
