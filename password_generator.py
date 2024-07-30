import string
import random

lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)
alphabet = lower_alphabet + upper_alphabet

numbers = list(string.digits)

symbols = list(string.punctuation)

password = ""
password_list = []

total_alphabet = int(input("How many alphabets do you want in your password? "))
total_number = int(input("How many numbers do you want in your password? "))
total_symbol = int(input("How many symbols do you want in your password? "))

for _ in range(total_alphabet):
    password_list += random.choice(alphabet)

for _ in range(total_number):
    password_list += random.choice(numbers)

for _ in range(total_symbol):
    password_list += random.choice(symbols)
     

password = ("Your password is: " + "".join(password_list))

print(password)