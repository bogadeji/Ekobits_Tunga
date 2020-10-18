1. ```
function myName() {
		let fullName = 'Abigail Adeboga';
		console.log(fullName);
	}
	```
2. let favoriteFoods = ['pizza', 'ice cream'];
3. ```
function randomFood() {
	let foodIndex = Math.floor(Math.random * favoriteFoods.length);
	return favoriteFoods[foodIndex]
}
```
4. let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
5. ```
function displayOddNumbers() {
		for(let number in numbers) {
			if (number%2 !== 0) {
				console.log(number)
			}
		}
	}
```
6. ```
function displayEvenNumbers() {
	for(let number in numbers) {
		if (number%2 === 0) {
			console.log(number)
		}
	}
}
```
7. ```
function returnFirstOddNumber() {
		for (let number in numbers) {
			if (number%2 !== 0) {
				console.log(number);
				break;
			}
		}
	}
```
8. ```
function returnFirstEvenNumber() {
		for (let number in numbers) {
			if (number%2 === 0) {
				console.log(number);
				break;
			}
		}
}
```
9. ```
function returnFirstHalf() {
	let firstHalfLength = numbers.length / 2
		return numbers.slice(0, firstHalfLength)
	}
```
10. ```
function returnSecondHalf() {
	let helfLength = numbers.length / 2
	return numbers.slice(halfLength)
}
```