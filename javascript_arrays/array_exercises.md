
`let people = ["Greg", "Mary", "Devon", "James"];`

1. ` for (let person of people) {
		console.log(person);
	 }`
2. `people.shift();`
3. `people.pop();`
4. `people.unshift('Matt');`
5. `people.push('Abigail');`
6. ``` for(let person of people) {
			console.log(person);
			if( person === "Mary") {
				break;
			}
		}```
7. `people.slice(2);`
8. `people.indexOf('Mary');`
9. `people.indexOf('Foo');`
10. ```let people = ["Greg", "Mary", "Devon", "James"];
		people.splice(2, 1, 'Elizabeth', 'Artie');```
11. `let withBob = people.concat("Bob")