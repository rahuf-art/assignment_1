# Input a word from the user
word = input("Enter a word: ")

# Check if the input is not empty
if len(word) > 0:
    reversed_word = ""
    # Iterate through the characters of the word in reverse order
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]

    # Display the reversed word
    print(f"Reversed word: {reversed_word}")
else:
    print("Please enter a valid word.")

