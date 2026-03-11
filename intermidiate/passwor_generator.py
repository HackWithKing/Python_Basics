import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

length = int(input("Enter password length: "))
print("Password:", generate_password(length))
