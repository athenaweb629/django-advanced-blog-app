const framework = 'Django'
const language = 'Python'
alert(framework + ' is written in ' + language)

  /* Note - Lines in javascript can be terminated with a semi colon. concatenated works the same as it does in python.
   */ 

  const name = 'Ben'
let benCount = 0
if (name === 'Ben') {
    benCount = 1
}

alert('There is ' + benCount + ' Ben')
/*
Contional statements - the 'IF' statment must have parentheses around it. For a single line 'if' statement, curly braces are not required, but sometimes it can be preferable to always use them to be very clear which parts of the code are inside the if body.
*/

/* 
Notice that we’re using triple-equals (===) to compare the variables in the condition. Using === means that the types of the items being compared are taken into comparison. For example, in JavaScript we could compare the string '1' and number 1 with ==. This would evaluate to true, as JavaScript coerces them to the same type and then compares. With === type coercion doesn’t take place, so '1' === 1 is false.
*/


// INVALID EXAMPLES: 

// const values cannot be reassigned. 
const pi = 3.14159
pi = 3  // trade accuracy for speed

// Variable fruitCount is not being reassigned, its being redefined. which is not allowed. 
let fruitCount = 5
let fruitCount = 6



// VALID EXAMPLES: 
// Variables defined with const are allowed to be mutated, so we could add items to an array or reassign values in an object (javascript object = python dict)

const fruit = ['Apple', 'Banana']
fruit.push('Cherry')  // append 'Cherry' to the end of the `fruit` list

const fruitCount = {Apple: 0, 'Banana': 1}
fruitCount.Cherry = 2  // add new item to object
fruitCount['Cherry'] = 2  // is equivalent

const myFruit = 'Cherry'
fruitCount[myFruit] = 2 // is also equivalent





/* Intro / Fundamentals Side Notes:

  - Arrays can be defined using square brackets [], equivalent to Python’s list.
  - We’re able to make changes to the fruit array and it doesn’t violate the const declaration because it’s mutating the object not reassigning the variable.
  - Objects are declared with curly braces {}, equivalent to Python’s dict.
  - The object keys don’t need to be quoted, {Apple: 0, 'Banana': 1} is the equivalent of {'Apple': 0, Banana: 1}.
  - Object items can be accessed with . notation, like Python properties/attributes.
  - Object items can also be accessed with square bracket notation, but must be quoted, or accessed with a variable. The equivalent of how you access items in a Python dict.
*/