import string
import random

# Create lists for different character types
lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)
alphabet = lower_alphabet + upper_alphabet
numbers = list(string.digits)
symbols = list(string.punctuation)

# Initialize an empty list to store the password characters
password_list = []

# Prompt user for input
try:
    total_alphabet = int(input("How many alphabets do you want in your password? "))
    total_number = int(input("How many numbers do you want in your password? "))
    total_symbol = int(input("How many symbols do you want in your password? "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

# Add random characters to the password list
for _ in range(total_alphabet):
    password_list.append(random.choice(alphabet))

for _ in range(total_number):
    password_list.append(random.choice(numbers))

for _ in range(total_symbol):
    password_list.append(random.choice(symbols))

# Shuffle the list to ensure random distribution
random.shuffle(password_list)

# Generate the final password string
password = "".join(password_list)

print(f"Your password is: {password}")
