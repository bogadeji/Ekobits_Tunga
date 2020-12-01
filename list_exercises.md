Given a list [1,2,3,4], print out all the values in the list.
```
for num in [1,2,3,4]:
	print(num)
```
or
```
print([val for val in [1,2,3,4]])
```
Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
```
for num in [1,2,3,4]:
	print(num*20)
```
or
```
print([(val * 20) for val in [1,2,3,4]])
```

Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).
```
print([word[0] for word in ["Elie", "Tim", "Matt"]])
```
Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
```
print([num for num in [1,2,3,4,5,6] if num % 2 == 0])
```
Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
```
print([val for val in [1,2,3,4] if val in [3,4,5,6]])
```
Given a list of words ["Elie", "Tim", "Matt"] return a new list with each word reversed and in lower case (['eile', 'mit', 'ttam']).
```
print([name[::-1].lower() for name in ['Elie', 'Tim', 'Matt']])
```
Given two strings "first" and "third", return a new string with all the letters present in both words (["i", "r", "t"]).
```
print([letter for letter in 'first' if letter in 'third'])
```
For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
```
print([num for num in range(2,100) if num%12==0])
```
Given the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).
```
print([letter for letter in 'amazing' if letter not in ['a', 'e', 'i', 'o', 'u']])
```
Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
```
print([[i for i in range(0,3)] for num in range(0,3)])
```
Generate a list with the value:
```
[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]
```

```
print([[i for i in range(0,10)] for num in range(0, 10)])
```