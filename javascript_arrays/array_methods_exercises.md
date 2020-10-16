# Part 1
`let arr = []`
`arr.push('Abigail')`
`arr.push('Adeboga')`
`arr.unshift('Blue')`

`arr.shift()`
`let arr2 = []`
`arr2.push(33)`
`arr2.push('JavaScript')`

`arr2.indexOf(42)` should return `-1` if the number 42 does not exist in the array

`let combinedArr = arr1.concat(arr2)`


# Part 2

`let arr = ["JavaScript", "Python", "Ruby", "Java"]`
1. `arr.slice(1, 3)`
2. `arr.concat("Haskell", "Clojure")`
3. `arr.join(", ")`
4. When a value is created and stored in a variable, an address is created in memory with that value, and the variable name points to that address in memory. 
Passing by value happens mostly with primitives. When a value is passed to a variable by value, the variable is assigned the value and references a new address in memory. So if the value of the first variable is changed, it doesn't affect the value of the second variable, as the values are picked from different addresses in memory.
```let instructor = 'Elie';
	let anotherInstructor = instructor;
	```
	At this point both `instructor` and `anotherInstructor` both have the same value, but what has happened is that `anotherInstructor` is assigned a copy of the value referenced by the variable `instructor`. The value for `anotherInstructor` however is assigned a different memory address. And so if the value of `instructor` is changed:
	```instructor = 'Matt'``` the value of `anotherInstructor remains the same. Because both variables are referencing two different memory addresses.

On the other hand, passing by reference assigns the value found in a memory address to the two variables
``` let instructors = ['Elie', 'Matt'];
	let instructorsCopy = instructors; ```
`instructorsCopy` points to the same memory address as `instructors`. And so if we have ```instructorsCopy.push('Bart');```, logging `instructors` will reflect the change made to `instructorsCopy`
