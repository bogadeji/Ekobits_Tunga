## Constructor functions
Javascript does not explicitly possess classes and objects as used in other object oriented languages. Constructor functions give us the ability to mirror what classes and objects do in other OOP languages. It helps set up blueprint or parent classes that can be inherited by other classes or objects(functions in javascript) that help us avoid unnecessary code duplication

## The `new` Keyword
When used to construct new objects, the `new` keyword does four things in succession
1. It creates an empty object
2. It assigns the keyword `this` inside of the constructor function to the empty object
3. It adds an implicit `return this` to the constructor function
4. It creates a link between the object it created and the `.prototype` property on the constructor function.

- The keyword `thi` inside of a constructor function refers to the object created using the constructor function

- A class is a template used for creating other objects. Objects created using a particular class inherit any initial values defined in the class, as well as any methods that class possesses. An instance of a class is a construction or instantiation of that class

- 
```
function Person (firstName, lastName, favoriteColor, favoriteNumber) {
	this.firstName = firstName;
	this.lastName = lastName;
	this.favoriteColor = favoriteColor;
	this.favoriteNumber = favoriteNumber;
	this.multiplyFunctionNumber = function(num){
		return num * this.favoriteNumber
	}
}
```

- Refactor the following code so that there is no duplication inside the Child function.

```
function Parent(firstName, lastName, favoriteColor, favoriteFood){
    this.firstName = firstName;
    this.lastName = lastName;
    this.favoriteColor = favoriteColor;
    this.favoriteFood = favoriteFood;
}

function Child(firstName, lastName, favoriteColor, favoriteFood){
    this.firstName = firstName;
    this.lastName = lastName;
    this.favoriteColor = favoriteColor;
    this.favoriteFood = favoriteFood;
}
```

// Refactored
```
function Parent(firstName, lastName, favoriteColor, favoriteFood){
    this.firstName = firstName;
    this.lastName = lastName;
    this.favoriteColor = favoriteColor;
    this.favoriteFood = favoriteFood;
}
```

```
function Child(firstName, lastName, favoriteColor, favoriteFood) {
	Parent.apply(this, arguments)
}
```