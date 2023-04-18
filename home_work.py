print("1. First")
print('--------')
#first
first_mass = [1, 2, 3, 4, 2, 5]
print(first_mass)

print("2. Second")
print('---------')
# second
first_mass.reverse()
print(first_mass)
first_mass.reverse()

print("3. Third")
print('--------')
#Third
LENTH_L=len(first_mass)
print(LENTH_L)

print("4. Forth")
print('--------')
# forth
My_lest=list(first_mass)
print(My_lest)
second_mass=[]

print("5. Fivth")
print('--------')
#fivth
my_arr = []
for item in range(6):
    if item % 3 == 0:
        my_arr.append(My_lest[item])
print(my_arr)

print("6. Six")
print('------')
# six
six_row=[1,4,4,6,4,1]
lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']

# To get the number of occurrences
# of each item in a list
print([[l, lst.count(l)] for l in set(lst)])

# To get the number of occurrences
# of each item in a dictionary
print(dict((l, lst.count(l)) for l in set(lst)))


print("7. seven")
print('--------')
#7. Seven
my_list=['Happy', 'New', 'Year']
seven_arr=[]
def seven(my_list):
    for i in range(3):
        seven_arr.append(len(my_list[i]))
        print(seven_arr)
    print(max(seven_arr))

seven(my_list)

print("8. Eight")
print('--------')

my_str="c/a/b/ded/a/"
my_finger=12
def divide_and_glue(my_str, my_finger):
    my_finger= my_str[::-1]
    print(my_finger)
divide_and_glue(my_str, my_finger)

print("9. Nine")
print('-------')
# 9. nine
# Input list
lst = [119, 101, 108, 108, 32, 100, 111, 110, 101]

print("Initial list : ", lst)
RES = ''.join(chr(i) for i in lst)
print("Final string : ", str(RES))
