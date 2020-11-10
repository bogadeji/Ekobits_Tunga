## printEvens
```
function printEvens(arr) {
	for (let i=0; i<arr.length; i++) {
		for (let j=0; j<arr[i].length; j++) {
			if (arr[i][j] % 2 == 0) {
				console.log(arr[i][j])
			}
		}
	}
}
```

## sumTotal
```
function sumTotal(arr) {
	let total = 0
	for (let i=0; i<arr.length; i++) {
		for (let j=0; j<arr[i].length; j++) {
			total += arr[i][j]
		}
	}
	return total
}
```

## countVowels
```
function countOnlyVowels(str, count) {
	let vowel = 'aeiou';
	str = str.toLowerCase()
	for (let i=0; i < str.length; i++) {
		if(vowel.includes(str[i])) {
			count++
		}
	}
	return count
}
function countVowels(arr) {
	let vowelCount = 0
	for (let i=0; i<arr.length; i++ ){
		if (Array.isArray(arr[i])) {
			for (let j=0; j<arr[i].length; j++) {
				vowelCount += countVowels(arr[i][j])
			}
		} else {
			vowelCount = countOnlyVowels(arr[i], vowelCount)
		}
		
	}
	return vowelCount
}

```

## rotate
```
function rotate(arr, num) {
	let newArr = arr.slice()
	let sliceArray = newArr.slice(0, newArr.length-num)
	let split = newArr.slice(-num)
	return split.concat(sliceArray)
}
```

## makeXOGrid
```
function makeXOGrid(rows, columns) {
let totalNumberOfXO = rows * columns
let totalXO = []

for (let i=0; i<totalNumberOfXO; i++){
	i%2 === 0 ? totalXO.push('X') : totalXO.push('O')
}
for (let i=0; i<rows; i++) {
	let cell = []
	cell.push(totalXO.splice(0, rows))
	
	totalXO.splice(totalXO.length,0,cell)
}
return totalXO
}
```
