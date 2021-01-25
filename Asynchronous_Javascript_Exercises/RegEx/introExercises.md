# Part I

## What is a regular expression? What are some use cases of regular expressions?
A regular expression is a sequence of characters that make up a pattern. RegEx is used to match complex string patterns

## What are the two ways to create regular expression in JavaScript?
- using the // notation
- using RegExp constructor

## What is a flag?
A flag is used when there is a need to match patterns accross all characters of a string. Without using a flag, only the first character to match the specified pattern is returned

## What is the difference between ?, + *?
`?` matches at most 1 of the character preceeding it.
`+` matches at least one of the character preceeding it.
`*` matches 0 or more of the charater preceeding it

## What is the difference between [] and {}?
`{}` is used to specify the specific quantity of one or more characters to be matched.
`[]` is used to specify a character set

## What does the search function do?
The search function returns the first starting point where a match is found within a string. If the match is not found, the function returns -1

## What do the exec and test functions do (these functions exist on the RegExp prototype)?
The `exec()` method executes a search for a match within a specified string. Its result is either an array or `null`.
The `test()` method is used to determine if a pattern is found in a string. It executes a search for a match between a regular expression and a specified string. Its result is boolean (either `true` or `false`)


# Part II
### countNumbers
```
function countNumbers(str){
    let regex = new RegExp(/[0-9]/, 'g')
    let matches = str.match(regex)
    return matches ? matches.length : 0
}
```

### capitalSentence
```
function capitalSentence(str) {
    let regex = new RegExp(/[A-Z]/, 'g')
    let matches = str.match(regex)
    return matches ? matches.join("") : null
}
```

### isValidPassword
```
function isValidPassword(str) {
    let regex = new RegExp(/[a-zA-Z0-9]{7,}[!@#$]+/, 'g')
    return regex.test(str)
}
```
### nothginSpecial
```
function nothingSpecial(str) {
   return typeof str === 'string' ? str.replace(/[^a-zA-Z0-9\s]/g, '') : 'Not a string!'
}
```
### sentenceCount
```
function sentenceCount(str) {
  let regex = new RegExp(/\?\.\!/, 'gi')
return str.match(regex) ? str.match(regex).length : 0
}
```