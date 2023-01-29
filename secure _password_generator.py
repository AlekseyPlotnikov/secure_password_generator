from random import *
from string import *


def how_many_passwords():
    while True:
        n = input('Сколько паролей вам нужно?\n')
        if n.isdigit():
            return int(n)


def length_password():
    while True:
        length = input('Какова нужна длинна паролей?\n')
        if length.isdigit():
            return int(length)


def generate_list():
    chars = ''
    is_digits = input('Нужно ли включать числа? [д/н][y/n]\n').lower() == ('д' or 'y')
    is_ascii_lowercase = input('Нужно ли включать прописные латинские буквы? [д/н][y/n]\n').lower() == ('д' or 'y')
    is_ascii_big = input('Нужно ли включать заглавные латинские буквы? [д/н][y/n]\n').lower() == ('д' or 'y')
    is_specials = input('Нужно ли включать символы: !#$%&*+-=?@^_ ? [д/н][y/n]\n').lower() == ('д' or 'y')
    is_isk = input('Исключить неоднозначные символы: il1Lo0O ? [д/н][y/n]\n').lower() == ('д' or 'y')
    if is_digits:
        chars += digits
    if is_ascii_lowercase:
        chars += ascii_lowercase
    if is_ascii_big:
        chars += ascii_uppercase
    if is_specials:
        chars += punctuation
    if is_isk:
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')

    return chars


def generate_password():
    print('Генератор паролей.')
    n = how_many_passwords()
    l = length_password()
    chars = generate_list()
    for _ in range(n):
        new_password = []
        for _ in range(l):
            new_password.append(choice(chars))
        print(''.join(new_password))


generate_password()
