# Random Password Generator

import random
import string

length = int(input("Password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

# string.ascii_letters == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits == 0123456789
# string.punctuation == !"#$%&'()*+,-./:;<=>?@[\]^_{|}~`

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated password:", password)