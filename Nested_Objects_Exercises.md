```
let nestedData = {
  innerData: {
    order: ["first", "second", "third"],
    snacks: ["chips", "fruit", "crackers"],
    numberData: {
        primeNumbers: [2,3,5,7,11],
        fibonnaci: [1,1,2,3,5,8,13]
    },
    addSnack: function(snack){
        this.snacks.push(snack);
        return this;
    }
  }
}
```
## primeNumbers
```
let primeNumbers = nestedData.innerData.numberData.primeNumbers
for (let i = 0; i < primeNumbers.length; i++) {
	console.log(primeNumbers[i])
}
```

## fibonacciNumbers
```
let fibonacciNumbers = nestedData.innerData.numberData.fibonacci
for (let i = 0; i < fibonacciNumbers.length; i++) {
	console.log(fibonacciNumbers[i])
}
```
## order
```
console.log(innerData.order[1])
```
## addSnack
```
nestedData.innerData.addSnack('chocolate')
```

The `this` keyword within the `addSnack` function refers to the whole `nestedData` variable.


```
let nestedObject = {
  speakers: [{name:"Elie"},{name:"Tim"},{name:"Matt"}],
  data: {
    continents: {
      europe: {
        countries: {
          switzerland: {
            capital: "Bern",
            population: 8000000
          }
        }
      }
    },
    languages: {
      spanish: {
          hello: "Hola"
      },
      french: {
          hello: "Bonjour"
      }
    }
  }
}
```

## addSpeaker
```
function addSpeaker(name) {
	nestedOject.speakers.push(
		{
			name: name
		})
}
```

## addLanguage
```
function addLanguage(newLanguage, helloInLanguage) {
	nestedObjects.data.languages[language] = {
		hello: helloInLanguage
	}
}
```

## addCountry
```
function addCountry(countryName, countryCapital, countryPopulation) {
	nestedobjects.data.continenets.europe.countries[countryName] = {
		capital: countryCapital,
		population: countryPopulation
	)
}
```