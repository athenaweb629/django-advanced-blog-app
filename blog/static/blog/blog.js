// Loops
for(let i = 0; i < 10; i += 1) {
  console.log('for loop i: ' + i)
}

let j = 0
while(j < 10) {
  console.log('while loop j: ' + j)
  j += 1
}

let k = 10

do {
  console.log('do while k: ' + k)
} while(k < 10)

const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.forEach((value => {
  console.log('For each value ' + value)
}))

const doubled = numbers.map(value => value * 2)

console.log('Here are the doubled numbers')

console.log(doubled)
/*
For loop
The first is to use a for() loop, which you’ll be familiar with if you’ve used other programming languages like C or Java.
A for loop consists of four parts:
An initializer, which is executed when the loop starts.
A condition, which is checked before each loop iteration. The loop only continues if the condition is true, otherwise the loop stops.
An advancement statement, which is executed at the end of each iteration to change the state of variables.
A loop body that is executed each iteration.
All parts of the for loop are optional.
Here’s a for loop that initializes with the statement let i = 0, which declares the variable i and sets it to 0. The condition is i < 10, which means the loop will run until i equals 9. The advancement is i = i + 1, that is, i is incremented after each iteration:
for(let i = 0; i < 10; i += 1) {
  console.log(i)
}
This prints the numbers 0 through 9 (inclusive) to the browser console.
While loop
while() loops behave the same as their Python equivalent. The loop body is executed until the condition is false. This while() loop behaves the same as the previous for loop we saw.
let i = 0

while(i < 10) {
  console.log(i)
  i += 1
}
Do-while loop
Do-while loops are like while loops, in that they execute until a condition is false, the difference is they will always be executed at least once. The condition comes at the end of the loop body. In this next example, the number 10 is printed once. Even though the condition is false, the loop body is already executed once before it is checked.
let i = 10

do {
  console.log(i)
  i += 1
} while(i < 10)
Other iterators
Instead of writing loops, we can iterate over arrays, which can be more idiomatic and a little bit more like Python. The two ways of doing this are the forEach() and map() methods. forEach() executes a function for each item in the array. map() also executes a function for each item in the array, but returns a new array of the same size, which contains the result(s) of the function.
Here’s how we could print the numbers 0 to 9 using forEach().
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.forEach((value => {
  console.log(value)
}))
Here’s how we could use map to double each of our numbers, into a new array called doubled.
const doubled = numbers.map(value => value * 2)

console.log(doubled)
Notice here the use of an anonymous, lambda function.




*/