### Part 1

- ```
var data = this;
console.log(data);
```
The value of the keyword `thi` in te above snippet is the window object

- ```
function logThis() {
	return this;
}
logThis();
```

The function above outputs the window object. Default binding applies here because the `this` keyword is in the global context.

- ```
var instructor = {
    firstName: 'Tim',
    sayHi: function(){
        console.log("Hello! " + this.firstName);
    }
}
instructor.sayHi()
```
The above function outputs 'Hello! Tim'. Implicit binding applies, the `this` keyword is in the context of the instructor object

- ```
var instructor = {
    firstName: 'Tim',
    info: {
        catOwner: true,
        boatOwner: true
    },
    displayInfo: function(){
        console.log("Cat owner? " + this.catOwner);
    }
}
instructor.displayInfo()
```
The function outputs 'Cat owner? undefined'. the instructor object (which is the context referred to by the `this` keyword) does not have a property catOwner. Using `this.info.catOwner` would access the catOwner property.

- ```
var instructor = {
    firstName: 'Tim',
    info: {
        catOwner: true,
        boatOwner: true,
        displayLocation: function(){
            return this.data.location;
        },
        data: {
            location: "Oakland"
        }
    },
}
instructor.info.displayLocation()
```
The function returns 'Oakland'. The `this` keyword used in the displayLocation property, refers to `instructor.info`.

- ```
var instructor = {
    firstName: 'Tim',
    info: {
        catOwner: true,
        boatOwner: true,
        displayLocation: function(){
            return this.location;
        },
        data: {
            location: "Oakland",
            logLocation: this.displayLocation
        }
    },
}
instructor.info.data.logLocation()
```
The function call returns TypeError. The `this` keyword as used in `instructor.info.data.logLocation` refers to it's direct parent, which is the `data` object. The `data` object however, does not have a `displayLocation` property. However for the function call to not return a TypeError, the property would have to be a method.


### Part 2

## Call Apply Bind Exercises
Fix the following code:

``` var obj = {
    fullName: "Harry Potter",
    person: {
        sayHi: function(){
            return "This person's name is " + this.fullName
        }
    }
}
```

```
obj.person.sayHi.call(obj);
obj.person.sayHi.apply(obj);
obj.person.sayHi.bind(obj)();
```


## List two examples of "array-like-objects" that we have seen.

- Arguments variables found in javascript functions
- DOM nodes

## Functions to write

# sumEvenArguments
```
function sumEvenArguments() {
	return [].slice.call(arguments).reduce(function(acc,next){
		if (next % 2 === 0)
			acc += next
        return acc
    },0)
}
```

# arrayFrom
```
function arrayFrom() {
	return [].slice.call(arguments)
}
```

# invokeMax
```
	function invokeMax(fn, num) {
	let counter = 0
	for (let i=0; i<=num; i++) {

	}
	return function() {
		counter++
		if (counter> num) {
			return 'Maxed Out!'
		}
		return fn.apply(this, [].slice.call(arguments))
	}
}
```

# guessingGame
	```
	function guessingGame(amount) {
	let answer = Math.floor(Math.random() * 10)
	let guesses = 0
	if(answer === 0) {
		return "No more guesses, the answer was 0"
	}
	return function(guess) {
		guesses++
		if (guesses > amount) {
			return "You are all done playing!"
		}

		if (guess === answer) {
			return "You got it!"
		} else if( guess < answer) {
			return "You're too low!"
		} else {
			return "You're too high!"
		}
	}
}```