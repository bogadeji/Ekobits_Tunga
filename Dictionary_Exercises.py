# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).
print({ k:v for (k,v) in [("name", "Elie"), ("job", "Instructor")]})

# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] return a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. You can research the zip method to help you.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
print({list1[i] : list2[i] for i in range(0, len(list1))})

# Create a dictionary with the key as a vowel in the alphabet and the value as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels = ['a', 'e', 'i', 'o', 'u']
print({vowel: 0 for vowel in vowels})

# Create a dictionary starting with the key of the position of the letter and the value as the letter in the alphabet. You should return something like this (Hint - use chr(65) to get the first letter):
print({ num : chr(num+64)  for num in range(1, 27)})