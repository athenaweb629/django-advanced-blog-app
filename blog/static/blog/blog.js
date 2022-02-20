// [Experiment 1] - Variables and their scopes (base code)

const theNumber = 1
let name = 'Hello!' // Second msg

if (theNumber === 1) {
  let name = 'Welcome to Blango' // First msg
  alert(name)
}

alert(name) 



/* [Experiment 2] - Change let name = 'Leo' to just name = 'Leo'

const theNumber = 1
let name = 'Ben' // Msg never shows

if (theNumber === 1) {
  name = 'Leo' // Msg shows twice in two separate alerts
  alert(name)
}

alert(name)
*/

/* [Experiment 3] - Remove the name declaration from the outer(Outside of the 'IF' statement) scope.


const theNumber = 1
//let name = 'Ben' 
// Ben is the name declaration in the outer scope

if (theNumber === 1) {
  let name = 'Leo' // Two msg alerts. first says leo. second is blank / empty.
  alert(name)
}

alert(name)
*/



/* [Experiment 4] - Change theNumber to something other than 1 so that (the) 'if' body is not executed.

const theNumber = 1
let name = 'Ben' // One alert message with 'Ben"

if (theNumber === 2) {
  let name = 'Leo' // No second alert and no msg with 'leo'
  alert(name)
}

alert(name)
*/