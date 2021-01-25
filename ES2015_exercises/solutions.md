# Convert the following es5 code blocks into es2015 code.
```
var person = {
    fullName: "Harry Potter",
    sayHi: function(){
        setTimeout(function(){
            console.log("Your name is " + this.fullName)
        }.bind(this),1000)
    }
}


let fullName = 'Harry Potter'

let person = {
    fullName,
    sayHi() {
        setTimeout(()=> {
            console.log(`Your name is ${this.fullName}`)
        }, 1000)
    }
}
```

```
var name = "Josie"
console.log("When " + name + " comes home, so good")


var name = "Josie"
console.log(`When ${name} comes home, so good`)
```

```
var DO_NOT_CHANGE = 42;
DO_NOT_CHANGE = 50; // stop me from doing this!

const DO_NOT_CHANGE = 42
```

```
var arr = [1,2]
var temp = arr[0]
arr[0] = arr[1]
arr[1] = temp


var [a,b] = [1,2]
[a,b] = [b,a]
```

```
function double(arr) {
    return arr.map(function(val) {
        return val*2
    })
}

function double(arr) {
    return arr.map(val=> val*2)
}
```

```
var obj = {
    number: {
        a:1,
        b:2
    }
}
var a = obj.numbers.a
var b = obj.numbers.b

var obj = {
    number: {
        a:1,
        b:2
    }
}

let {a,b} = obj.number
```

```
function add(a,b) {
    if(a === 0) a = 0
    else {
        a = a || 10
    }
    if(b === 0) b = 0
    else {
        b = b || 10
    }
    return a + b
}

function add(a=10, b=10) {
    return a + b
}
`or`
let add = (a=10, b=10) => a + b
```