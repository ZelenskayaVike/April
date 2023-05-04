# import random

########### what decorator must look like
def retry(attempts=5, desired_value=None):
    def wrapper(*args, **kwargs):
        print("ARGS & KWARS")
        print(args,kwargs)
        print("FUNK")
        return get_random_value(args, kwargs)
    if attempts==5:
        return wrapper
    else:
        print("Error")
        return wrapper(2,3)
@retry
def get_random_value_with_default_attempts():
    print("first")
    return random.choice((1, 2, 3, 4, 5))



@retry
def get_random_values_with_default_attempts(choices, size=2):
    return random.choices(choices, k=size)


@retry
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


# ########### examples of function usages
get_random_value()
# get_random_value_with_default_attempts()
# get_random_values_with_default_attempts([1, 2, 3, 4])
# get_random_values_with_default_attempts([1, 2, 3, 4], 2)
# get_random_values_with_default_attempts([1, 2, 3, 4], size=2)
# get_random_values_with_default_attempts(choices=[1, 2, 3, 4], size=2)
# get_random_values([1, 2, 3, 4])
# # get_random_values([1, 2, 3, 4], 3)
# get_random_values([1, 2, 3, 4], size=1)
