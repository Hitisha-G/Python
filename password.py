# random password generator

import random

def get_char(char_list,num):
    temp_list=[]
    for i in range(num):
        temp_list.append(random.choice(char_list))

    return temp_list

# def get_sym(sym)

while True:
    num_char= int(input('Number of chars :'))
    num_upper=int(input('number of upper:'))
    num_sym=int(input('number of symbols:'))
    if num_char< num_upper + num_sym:
        print("less char")
    else:
        break

upper_list=[chr(i) for i in range(65, 65+26)]
upper_char = get_char(upper_list, num_upper)
sym_list=[chr(i) for i in range(32,48)]
sym_list+=[chr(i) for i in range(58,65)]
sym_char= get_char(sym_list,num_sym)

num_unfilled = num_char - num_upper - num_sym
# print(num_unfilled)
whole_list = upper_list + sym_list
rem_char = get_char(whole_list, num_unfilled)
# print(rem_char)
password = upper_char + sym_char + rem_char
# print(password)
# fixed order here hence shuffle

random.shuffle(password)

password = ''.join(password)

print(password)
