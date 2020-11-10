# Higher Order Functions
## map
```
function map(arr, mapCallback){
	return callback(arr)
}

function mapCallback(arr) {
	for (let i=0; i<arr.length; i++) {
		arr[i] * 2
	}
}
```

## reject
```
function reject(arr, callback) {
	return callback(arr)
}
```

#Timers
`SetTimeout` will only run the callback function to be executed once, `SetInterval` runs the callback function until the timer is cleared.

`SetInterval` is more or less a timed loop, and should be used when the exact time interval that an event occurs is important. Otherwise, a simple loop works just as well.

The first parameter that both timers accept is a callback function

The stored result of the timers can be used to stop them. If there is a need to stop any of the timers because a condition has been met, storing the result makes that possible.

Code or functions that are not timed, would run before any within either of the timers.

# Closures
Closer refers to the ability of function to access variables from it's parent scope, even after the parent function has closed and returned a value

### Usefulness of closures
- They make it possible to create private variables in JavaScript
- Modules

A module is a piece of code that is encapsulated and reuseable

`arguments` is an array-like object accessible inside functions. It contains the values of the arguments passed to that function. It is not available to arrow functions.

It has the length property similar to arrays, and it's properties are indexed from zero (just like arrays), but it doesn't have any of the built-in methods available to Arrays

```
function createCounter() {
	let count = 0;
	return function() {
		count++
		return count
}
}
```

# Higher Order Functions, Timers and Closures Exercises

## countdown
```
function countdown(num) {
	let timerId = setInterval(()=> {
		num--
		if(num <= 0){
			clearTimeout(timerId)
			console.log('DONE!')
		} else {console.log(num)}
		},1000)
		
}
```

## randomGame
```
function randomGame() {
	let counter = 0
	let timerId = setInterval(()=> {
		let randomNumber = Math.random()
		counter++
		if(randomNumber > 0.75) {
			clearTimeout(timerId);
			console.log(counter)
		}
		}, 1000)
}
```

## isEven
```
function isEven(num) {
	return num%2 == 0
}
```

## isOdd
```
function isOdd(num) {
	return num%2 != 0
} 
```

## isPrime
```
function isPrime(num) {
	for(var i = 2; i <= Math.sqrt(value); i++) {
        if(value % i === 0) {
            return false;
        }
    }
    return value > 1;
}
```

## numberFact
```
function numberFact(num, callback) {
	return callback(num);
}
```

## find
```
function find(arr, callback) {
	for(let i=0; i<arr.length; i++) {
		if( callback(arr[i])) { return arr[i]}
	}
}
```

## findIndex
```
function findIndex(arr, callback) {
	for(let i=0; i<arr.length; i++) {
		if( callback(arr[i])) { return i}
	}
}
```

## specialMultiply
```
function specialMultiply(a, b) {
	if (!arguments[1]) {
		return function(b) {
			return a * b
		}
	}		
	return a * b
}
```


