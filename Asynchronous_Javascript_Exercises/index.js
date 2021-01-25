//Write a function called inOrder that accepts two callbacks and invokes them in order. Implement inOrder using the callback pattern.

var logOne = setTimeout(function() {
    console.log("one!");
  }, Math.random() * 1000);
  
  var logTwo = setTimeout(function() {
    console.log("two!");
  }, Math.random() * 1000);

  function inOrder(first, second) {
      first(second)
  }
  // Using promises

function inOrder(first, second) {
  return () => first .then(()=>second)
}
inOrder(logOne, logTwo);


// Using promises

function inOrder(first, second) {
  return () => first .then(()=>second)
}