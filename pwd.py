# pwd.py
# random password generation
import random


def get_char():
    # define character set
    number_set = "0123456789"
    upper_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_set = "abcdefghijklmnopqrstuvwxyz"
    sign_set = ",.-"

    # combine character sets
    char_set = number_set + upper_set + lower_set + sign_set

    # randomly select a character from the character set to return
    return random.choice(char_set)


def generation(length=10, method=0):
    password = ""
    
    # select a total of length random characters
    for i in range(length):
        password = password + get_char()
    return password


if __name__ == '__main__':
    print(generation(15))
