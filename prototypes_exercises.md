### Part 1

- 
```
function Person(firstName, lastName, favoriteColor, favoriteNumber) {
	this.firstName = firstName
	this.lastName = lastName
	this.favoriteColor = favoriteColor
	this.favoriteNumber = favoriteNumber
	this.favoriteFoods = []
	this.family = []
}
```

```
Person.prototype.fullName = function() {
	return this.firstName + ' ' + this.lastName
}
```

```
Person.prototype.toString = function() {
	return `${this.fullName()}, Favorite Color: ${this.favoriteColor}, Favorite Number: ${this.favoriteNumber}`
}
```

```
Person.prototype.addToFamily = function(familyMember){
	if(familyMember instanceof Person && !this.family.includes(familyMember)) {
		this.family.push(familyMember)
	}
	return this.family.length
}
```

### Part 2

## Array.prototype.map
```

```

## String.prototype
```

```

## Function.prototype.bind
```

```

###  Part 3

For the last part, let's think less about the actual code we need to write and more about thinking in an Object Oriented way.

Let's imagine that we are building an application which allows users to play chess. What constructor functions would we need? What kinds of prototype functions and properties would we need as well?

Let's imagine that we are building a game of Tic Tac Toe. What kinds of prototype functions and properties would we need as well?
