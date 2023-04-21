import random
import string
import time

my_arr=[]

def my_sum(my_arr):
    if len(my_arr) == 0:
        return 0
    return my_sum(my_arr[:-1])+my_arr[-1]
my_arr=[1,3,2,3,23,12]
print(my_sum(my_arr))


#2. Задача 2in
#
my_list=["aple", "orange", "pepci", "Cola", "tomato", "potaito"]
#
# my_bloke=[]
def word_play(my_list, numb):
    if numb<len(my_list):
        my_bloke=my_list[0:(len(my_list)-numb)]
        print(my_bloke)
    if numb==len(my_list):
        my_bloke=my_list
        print(my_bloke)
    if numb>len(my_list):
        my_rez= numb-len(my_list)
        my_bloke=my_list+my_list[0:my_rez]
        print(my_bloke)

word_play(my_list, 6)
word_play(my_list, 3)
word_play(my_list, 11)

#3. task
PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))
def password_checker(password):
    password = input("wright the password")
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char == passed_pass_char:
            print("You well come")
            password = input("Wrighе the password")
        else:
            password = input("Wrighе the password")
            print("error")

        time.sleep(0.1)
password_checker("")
