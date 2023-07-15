import string
import random

lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)


def lowergen(password):
    list_of_lower = random.sample(lowerCase, random.randint(0, 4))
    password += list_of_lower
    return password


def uppergen(password):
    list_of_upper = random.sample(upperCase, random.randint(0, 4))
    password += list_of_upper
    return password


def numbergen(password):
    list_of_numbers = random.sample(numbers, random.randint(0, 4))
    password += list_of_numbers
    return password


def symbolgen(password):
    list_of_symbols = random.sample(symbols, random.randint(0, 4))
    password += list_of_symbols
    return password


def password_generator():
    password = []
    while len(password) < 8:
        rand = random.randint(1, 4)
        if rand == 1:
            lowergen(password)
        elif rand == 2:
            uppergen(password)
        elif rand == 3:
            numbergen(password)
        elif rand == 4:
            symbolgen(password)
    return ''.join(password[0:8])
