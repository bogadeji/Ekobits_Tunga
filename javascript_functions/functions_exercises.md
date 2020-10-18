# Part 1

## difference
```
function difference(a, b) {
	return a - b;
}
```

## product
```
function product(a, b) {
	return a * b;
}
```

## printDay
```
function printDay(number) {
	switch (number) {
		case 1:
		return 'Sunday';
		break;
		case 2:
		return 'Monday';
		break;
		case 3:
		return 'Tuesday';
		break;
		case 4:
		return 'Wednesday';
		break;
		case 5:
		return 'Thursday';
		break;
		case 6:
		return 'Friday';
		break;
		case 7:
		return 'Saturday';
		break;
		default:
		return undefined;
	}
}
```

## lastElement

```
function lastElement (arr) {
	return arr.length < 1 ? undefined : arr[arr.length - 1]
}
```

## numberCompare
``` 
function numberCompare (numb1, numb2) {
	const diff = (numb1 - numb2)

	if (diff > 0) {
		return 'First is greater';
	} else if (diff < 0) {
		return 'Second is greater';
	} else {
		return 'Numbers are equal';
	}
}
```

## singleLetterCount
```
function singleLetterCount(word, letter) {
	let word = word.toLowerCase();
	let letter = letter.toLowerCase();

	let count = 0;
	for (let i = 0; i < word; i++) {
		if(word[i] === letter) {
			count++;
		}
		return count;
	}
}
```


# Part 2

## multipleLettercount
```
function multipleLetterCount(str) {
	const countObj = {};

	for (let i=0; i < str.length; i++ ) {
		let letter = str[i];
		if (countObj[letter] === undefined) {
			countObj[letter] = 1;
		} else {
			countObj[letter] += 1;
		}
	}
	return countObj;
}
```

## arrayManipulation
```

	if (command === 'remove') {
		if (location == 'end') {
			return arr.pop();
		} else if (location === 'beginning') {
			return arr.shift();
		}
	} else if (command === 'add') {
		if (command === 'add' && location === 'beginning') {
			return arr.unshift('value');
		} else if (command === 'add' && location === 'end') {
			return arr.push('value')
		}
	}
}
```

```
function arrayManipulation(arr, command, location, value) {
	if(command === 'remove') {
		return location === 'end' ? arr.pop() : arr.shift;
	} else if (command === 'add') {
		if (!value) { return "Input a number or string!"}
		return location === 'beginning' ? arr.unshift('value') : arr.push('value')
	}
}
```

## isPalindrome

```
function isPalindrome(str) {
	str = str.replaceAll("[^A-Za-z]+", "").toLowerCase();

	let reversedString = str.split("").reverse().join("");
	return str === reversedString;
}
```
# Part 3

```
const playerInput = prompt("Type 'Rock', 'Paper', or 'Scissors'")

const selection = [
    'rock', 'paper', 'scissors'
]

const rules = {
  	'rock': ['lizard', 'scissors'],
 	'paper': ['rocks', 'spock'],
 	'scissors': ['paper', 'lizard'],
}

const computerSelectionIndex = Math.round(Math.random() * (selection - 1));
const computerSelection = selection[computerSelectionIndex]


if(selection.indexOf(playerInput) > 0) {
	playerInput = prompt("Type 'Rock', 'Paper', or 'Scisssors'")
} else {
	const playerSelection = playerInput.toLowerCase();
	rockPaperScissors(playerSelection, computerSelection)
}

function rockPaperScissors(playerSelection, computerSelection) {
      if(playerSelection == computerSelection) {
        return 'It\'s a tie!!'
      } else {
      if (rules[computerSelection].includes(playerSelection.toLowerCase())) {
        return 'Computer wins!!!'
      }
      if ( rules[playerSelection].includes(computerSelection.toLowerCase())) {
        return 'YOU WIN!!!'
      }
    }
}
```