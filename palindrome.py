# take user input
user_input = input("Enter a string: ")

# remove all white spaces and convert to lowercase
user_input = user_input.replace(" ", "").lower()

# reverse the string
reverse_input = user_input[::-1]

# check if the string is equal to its reverse
if user_input == reverse_input:
    print(f"{user_input} is a palindrome")
else:
    print(f"{user_input} is not a palindrome")

