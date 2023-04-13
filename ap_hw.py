my_numbers = [20, 20, 30, 30, 40]
def get_unique_numbers(*args):
    args = my_numbers
    unique = []
    for number in my_numbers:
        if number in unique:
            continue
    return unique


print(get_unique_numbers(my_numbers))

# second
d_mass = {}


def get_request(**kwargs):
    assert isinstance(kwargs, dict)
    kwargs['use_tipe'] = "Student"
    for key in kwargs:
        d_mass.pop(key, kwargs[key])
        len(d_mass)
    return kwargs


print(get_request(apple='red', size='big', teste="good"))
print(d_mass)
print(len(d_mass))


# third

def combined_example(pos1, pos2, pos_only, /, standard, *, kwd_only_f, kwd_only_d, kwd_only_f_s):
    print(pos1, pos2, pos_only, standard, kwd_only_f, kwd_only_d, kwd_only_f_s)


combined_example(1, 1, 1, standard=2, kwd_only_f=3, kwd_only_d=3, kwd_only_f_s="hellow")


# foth

def first_funk(first_figer):
    def second_funk(second_figer):
        return first_figer * second_figer

    return second_funk


print(first_funk(2)(2))


# six
def six_funk(the_number):
    print("*" * the_number)
    print("*" * the_number)
    print("*" * the_number)
    print("*" * the_number)


six_funk(4)
