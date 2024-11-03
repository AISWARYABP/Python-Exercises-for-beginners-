def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Input from the user
user_input = input("Enter a word or phrase to check if it's a palindrome: ")

# Check and display the result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
