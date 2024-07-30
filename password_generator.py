#imports two modules string and random
import string
import random

#uses the string module and converts them to list and stores it in appropriate variable
lower_alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)
alphabet = lower_alphabet + upper_alphabet

numbers = list(string.digits)

symbols = list(string.punctuation)

#creates a password string to later store the generated password in  
password = ""

#creates a list "password_list" to append to it the randomly generated characters
password_list = []


#prompts the user to input how many alphabets, numbers and symbols
total_alphabet = int(input("How many alphabets do you want in your password? "))
total_number = int(input("How many numbers do you want in your password? "))
total_symbol = int(input("How many symbols do you want in your password? "))


#adds the random choice from alphabet, numbers and symbols
for _ in range(total_alphabet):
    password_list += random.choice(alphabet)

for _ in range(total_number):
    password_list += random.choice(numbers)

for _ in range(total_symbol):
    password_list += random.choice(symbols)

#shuffles the password_list list to have random distribution
random.shuffle(password_list)

#adds the generated password to the password variable
password = ("Your password is: " + "".join(password_list))

print(password)