import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789;_[]()' # CAN Add more things

while 1:
    pwd_len = int(input('What length would you like you password be: '))
    pwd_count = int(input('How many passwords would you like:'))
    for x in range(0, pwd_count):
        pwd = ''
        print('\n')
        for y in range(0, pwd_len):
            pwd_char=random.choice(chars)
            pwd = pwd + pwd_char
        print('Here is ur password: ' + pwd)
    break