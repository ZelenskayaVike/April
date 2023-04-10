def maximum_number(first_number, second_number):
    if first_number > second_number:
        print(first_number, 'is max')
    elif first_number == second_number:
        print(first_number, 'is equal to', second_number)
    else:
        print(second_number, 'is max')
maximum_number(3,4)
maximum_number(4,5)
# 2second
def high_number(one_number,two_number,three_number):
    if one_number > two_number and one_number>three_number:
        print(one_number, 'is maximum')
    if two_number>one_number and two_number>three_number:
        print(two_number, 'is max')
    else:
        print(three_number, 'is maximum')
high_number(6,4,5)
high_number(6,33,5)
#second
# 3third
def modul_number(figer):
    if figer > 0:
        print(figer)
    else:
        print(-figer)
modul_number(-5)

# forth
def funk_foth(humber_one,number_two):
    return humber_one+number_two
print(funk_foth(3,4))

#six
def fun_six(the_number):
    if the_number>0:
        return "+"
    if the_number==0:
        return "=0"
    else:        return "-"

print(fun_six(-4))
print(fun_six(4))
print(fun_six(0))
