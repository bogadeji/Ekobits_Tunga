# Write the following functions
from collections import Counter
# difference
def difference(a, b):
	return a - b

# product
def product(a, b):
	return a * b

# print_day
def print_day(num):
	days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	if 1 < num > 7:
		return none
	return days[num-1]

# last_element
def last_element(val: list):
	if not len(val):
		return None
	return val[len(val) - 1]

# number_compare
def number_compare(a: int, b: int):
	if a > b:
		return 'First is greater'
	elif a < b:
		return 'Second is greater'
	else:
		return 'Numbers are equal'

# single_letter_count
def single_letter_count(a: str, b: str):
	word = a.lower().split()
	return word.count(b.lower())

# multiple_letter_count
def multiple_letter_count(a: str) ->dict:
	return {letter: a.count(letter) for letter in a}

# list_manipulation
def list_manipulation(func_list: list, command, location, val):
	if command == 'remove':
		if location == 'end':
			return func_list.pop()
		elif location == 'beginning':
			return 
			 m func_list.pop(0)
	elif command == 'add'
		if location == 'end':
			func_list.insert(0, value)
		elif location == 'beginning':
			func_list.insert(len(func_list)-1, value)

		return func_list
# is_palindrome
def is_palindrome(palindrome):
	return palindrome == palindrome[::-1]

# frequency
def frequency(a:list, b):
	return a.count(b)
# flip_case
def flip_case(string, letter):
	flipped_string = [char.swapcase()  if char.upper() == letter.upper() else char for char in string]
	return ''.join(flipped_string)

# multiply_even_numbers
def multiply_even_numbers(num:list):
	final_multiple = 1
	for x in num:
		if x % 2 == 0:
			final_multiple*= x
	return final_multiple
# mode
def mode(lst):
    list_count = {val:lst.count(val) for val in lst}
    max_index = list(list_count.values()).index(max(list_count.values()))
    return list(list_count.keys())[max_index]
# capitalize
def capitalize(str):
	return str.capitalize()

# compact
def compact(collection:list):
	return [collection_value for collection_value in collection if collection_value]

# partition
def partition(collection, callback):
	one = []
	two = []
	for x in collection:
		if callback(x):
			one.append(x)
		else:
			two.append(x)
	return [one, two]
# intersection
def intersection(list1, list2):
	return [val for val in list1 if val in list2]
# once
def once(fn):

def run_once(callback):
    callback.counter = 0
    def inner(*args):
    	if callback.counter >= 1:
    		return None
    	else:
    	    callback.counter+=1
    	    print(callback.counter)
    	return callback(*args)
    return inner

  # PART 2
  # Reversed Strings https://www.codewars.com/kata/reversed-strings
  def reversed_strings(str):
  	return str[::-1]


# Looking for a benefactor https://www.codewars.com/kata/looking-for-a-benefactor

def donation_avg(arr, navg):
  	total_number = len(arr) + 1
  	arr_sum = sum(arr)
  	donation = (navg * total_number) - arr_sum
  	if donation < 0 :
  		return None
  	return donation

# Sum of a sequence https://www.codewars.com/kata/sum-of-a-sequence/

def sequence_sum(begin, end, step):
	sequence_list =[val for val in range(begin, end+1, step)]
	
	return sum(sequence_list)

# Max diff https://www.codewars.com/kata/max-diff-easy-1/python

def max_diff(collection: list):
	if len(collection) <= 1:
		return 0
	collection.sort()
	return collection[len(collection)-1] - collection[0]

# Count the smiley faces! https://www.codewars.com/kata/583203e6eb35d7980400002a/
def count_smileys(collection):
	valid_smileys = [':)', ':D', ';)', ';D', ':-)', ';-)', ';-D', ':-D', ';~)', ':~)', ':~D', ';~D']
	smileys = 0
	for str in collection:
		if str in valid_smileys:
			smileys+=1
	return smileys

# Sentence Count https://www.codewars.com/kata/sentence-count
def sentence_count(paragraph):
	return sum(paragraph.count(i) for i in '.?!')


# Tortoise Racing https://www.codewars.com/kata/tortoise-racing
def tortoise_racing(speed_a, speed_b, lead):
    if speed_a >= speed_b:
        return None
    time = lead / (speed_b -speed_a)
    return [int(time), int(time*60)%60, int(time*3600)%60]

# Calculate String Rotation https://www.codewars.com/kata/calculate-string-rotation
def string_rotation(str1, str2):
    for i in range(len(str1)):
        if str1 == str2[i:] + str2[:i]:
            return i
    return -1

