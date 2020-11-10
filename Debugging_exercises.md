# Part 1
- The `throw` keyword allows an application developer to return an error and stop code execution when something is being done incorrectly.
- The `finally` keyword is used by the applicaction developer to execute a piece code regardless of any errors thrown
- The difference between `TypeError` and `Reference Error`: While a `Reference Error` is thrown when there is an attempt to access a variable that does not exist in the scope which is it being called, `TypeError` is thrown  when there is an incorrect use of certain types, like trying to call something that is not a function or accessing properties on `undefined`
- To create a snippet in devtools, from within the sources tab in devtools, click on the `Snippets` tab. In the empty space within the `Snippets` tab, right click and select new. 
- An `exception` is an event that disrupts code/program execution.
- Catch errors in Javascript using `try / catch` statements
```try {
		thisDoesNotExist;
	} catch(e) {
		console.log("The error is ", e)
	}
```


1. `ReferenceError`. The variable does not exist in the globala scope
2. `TypeError` data.displayInfor is `undefined`, and so trying to invoke `undefined` will  result in `TypeError`
3. `TypeError` `data.displayInfo` is undefined. Trying to access a property of undefined results in TypeError
4. `ReferenceError` The variable does not exist in the scope in which it is being called

# Part 2
1. ```
for (let i = 0; i < 5; i ++) {
	console.log(i);
}
```
The condition within the for loop was wrong
2. ```
function addIfEven(num){
	if(num % 2 === 0) {
		return num + 5;
	}
	return num;
}
```
`=` is an assignment operator, not a comparison operator. The correct operator to use is either `==` or `===`
3. ```
function loopToFive() {
	for (let i=0; i<=5, i++) {
		console.log(i)
	}
}
```
or
```
function loopToFive() {
	for (let i=0; i<6; i++) {
		console.log(i)
	}
}
```
Semicolons are used to separate each section in the for loop, not commas                                               
The for loop would have stopped at `i = 4` since the condition states that `i` has to be less than 5. To loop to 5, the condition needs to change to include a fifth iteration

4.```
function displayEvenNumbers(){
    let numbers = [1,2,3,4,5,6,7,8];
    let evenNumbers = [];
    for(let i=0; i<numbers.length-1; i++){
        if(numbers[i] % 2 === 0) {
            evenNumbers.push(numbers[i]);
        }
    }
        return evenNumbers;
}
displayEvenNumbers();
```
There shouldn't be semicolons after the condition in the if statement or after the last section of the for loop. In the case of the semicolon after the increment in the for loop, the function will work regardless.
The loop condition should be `i < numbers.length` or `i < numbers.length - 1`
In the if statement, the condition should be `if (numbers[i]...	` not `if (numbers...`
`=` is an assignment operator, not a comparison operator. The correct operator to use is either `==` or `===`
numbers[i] is what needs to be pushed into the `evenNumbers` array, not `i`
The return statement should come after the for loop, not after the if statement.



