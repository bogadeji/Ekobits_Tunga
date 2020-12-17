# get_next_multiple
# This function should accept a number and return the next number that is divisible by it.

def get_next_multiple(num):
    new_num = num
    while True:
        new_num += num
        yield new_num
	
for a in get_next_multiple(14):
    print(a)

# is_prime
# This function should accept a number and return True or False if the number is a prime number.
def is_prime(num):
    if num > 2:
        if num%2 == 0:
            return False
        else:
            for i in range(2, int(num/2)):
                if num% i == 0:
                    return False
            return True
    elif num == 2:
        return True
    else:
        return False


# get_next_prime
# This function should return a generator that yields in the next prime number. The highest it should go should be 1000.
# Using the is_prime function defined above
def get_next_prime(num):
	for a in range(num, 1000):
		if is_prime(a):
			yield a


# double_result
# This decorator function should return the result of another function multiplied by two
from functools import wraps
def double_result(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return inner


# only_even_parameters
# This decorator function should only allow a function to have even parameters or else return the string "Please only use even numbers!"
from functools import wraps
def only_even_parameters(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(all([arg for arg in args if arg % 2 == 0]))
        if any([arg for arg in args if (arg % 2 != 0)]):
            return "Please add even numbers"
        else:
            return func(*args, **kwargs)
    return inner
	

# sum_index
# This function should accept a list or tuple and return the sum of each index. As a bonus, make this function able to accept a variable number of arguments.
def sum_index(*args):
	sum =0
	for ids, value in enumerate(*args):
		sum+=ids
	return sum
