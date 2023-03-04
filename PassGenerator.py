import string
import random

# specify the length of the password
password_length = 12

# define the pool of characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# generate a random password
password = ''.join(random.choice(characters) for i in range(password_length))

# print the password
print("Randomly generated password:", password)

