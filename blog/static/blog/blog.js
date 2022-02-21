// Console Logging 

console.time('myTimer')
console.count('counter1')
console.log('A normal log message')
console.warn('Warning: something bad might happen')
console.error('Something bad did happen!')
console.count('counter1')
console.log('All the things above took this long to happen:')
console.timeEnd('myTimer')




/* 
NOTE: console is a global variable, log() is a method of console;

                console.log('Hello, world')

But there are some other methods that are also useful:

- error(): Output a message at error level.

- warn(): Output a message at warning level.

- count(): Called with a label (e.g. console.count('foo')) and will output a count of how many times it has been called with that label.

- time(): Called with a name to start a named timer. (e.g. console.time('myTimer')), and then to output the time since the start, use…

- timeEnd(): Call this with the same label to output the time, in milliseconds, since the corresponding time() method was called.
*/

/* 
NOTE: The method of showing the JavaScript console depends on your browser and operating system.


- Chrome - On a Mac, it can be found under the View menu, then Developer, then JavaScript Console. On Windows, click on Tools and then Developer Tool. In the developer tools, you can click on the Console tab. You can also press the F12 key.

- Firefox - On a Mac, it can be found under the Tools menu, go to Browser Tools then Web Developer Tools. Then, select the Console tab. On Windows, click on Web Development and then Web Console. You can also press the F12 key.

- In Safari, you’ll need to enable the Develop menu. In the Safari preferences, select the Advanced tab then check Show Develop menu in the menu bar. Once you’ve done that, just choose Show JavaScript Console from the Develop menu.

*/



// Functions 
/*
In JavaScript there are a number of ways to define functions. The first way is similar to Python, using the function keyword which is similar to def in Python. Function bodies are contained inside curly braces ({}) and indentation doesn’t matter. Even though the lack of or inconsistent use of indentation will not cause an error, you should continue to use indentation to help with legibility. Also like Python, values can be returned from functions using return. Here’s a function in Python that adds two numbers together and returns the sum:

- python: 

def add_numbers(a, b):
    return a + b


- javascript equivalent: 

function addNumbers(a, b) {
    return a + b
}



In Javascript the convention for variables and function names is camelCase whereas in Python, we'd usually use snake_case


calling a function:

const result = addNumbers(3, 4)
console.log(result)

This will output 7 to the browser console.


Arguments to JavaScript functions are implicitly all optional. For example, in Python we would implement optional arguments like this:


def say_hello(name=None):
    if name is None:
        print("Hello, no name")
    else:
        print("Hello, " + name)

say_hello()  # name is None
say_hello("Lily")  # name is "Lily"



In JavaScript, we need to check if a variable is === to undefined, which means it hasn’t been passed in. This JavaScript function is roughly identical to the Python one:



function sayHello(name) {
  if (name === undefined) {
      console.log('Hello, no name')
  } else {
       console.log('Hello, ' + name)
  }
}

sayHello()  // name is undefined
sayHello('Lily')  // name is 'Lily'



Functions can also be assigned to variables. Another way of defining the sayHello() function is like this:



const sayHello = function(name) {
    if (name === undefined) {
        console.log('Hello, no name')
    } else {
        console.log('Hello, ' + name)
    }
}

sayHello('Lily')




Notice the function is called in the same way. Defining functions in this way is useful if you want to nest functions inside other functions and follow the variable scoping rules that we saw in the last section. Or, if you want to reassign functions to different variables (assuming you used let instead of const when assigning the function initially).
The third way of defining functions is to use anonymous or arrow functions, so called because they’re denoted with the => (“arrow”) operator, and they’ll be anonymous or unnamed unless they’re assigned to a variable. Here’s the sayHello function again:
const sayHello = (name) => {
  if (name === undefined) {
      console.log('Hello, no name')
  } else {
       console.log('Hello, ' + name)
  }
}
What’s the difference between using => or the function keyword? The context in which the function executes is different. We’ll come back to this later when dealing with classes, as it’s mostly only important then.
Using the arrow function also allows us to define lambda functions, that is, basic one-line functions that implicitly return a value. These are defined without the use of curly braces or the return keyword.
For example, here’s an arrow function that doubles a number:
const doubler = (x) => { return x * 2 }

console.log(doubler(2))  // outputs 4
And here’s the equivalent as a lambda:
const doubler = x => x * 2
Note that lack of curly braces or return. When using a single argument, the parentheses around the argument are optional.
Let’s look at a practical example of when anonymous functions are useful. They’re very short to write as callbacks, and a lot of JavaScript code is callback-based.
JavaScript provides a setTimeout() function. This will wait a number of milliseconds and then call a function that is passed to it. In this example, setTimeout wait 2 seconds (2,000 ms) and then calls the showAnAlert() function:
function showAnAlert() {
  alert('Timeout finished.')
}


setTimeout(showAnAlert, 2000)
This works OK for this function that takes no arguments, but how can we use setTimeout if a function needs arguments? A common pattern in JavaScript is to pass anonymous functions and use them as wrappers.
Let’s return to our sayHello() function again. Let’s say we want to wait 2 seconds, then greet the user with their name. We could do something like this:
const name = 'Ben'

setTimeout(() => {
    sayHello(name)
  }, 2000
)
Here we’re defining an anonymous function that takes no arguments (the empty parentheses () before the =>), and immediately passing it to setTimeout(). When it’s called, it accesses the name variable from the outer scope, and passes it to sayHello().
Let’s see this in action.
*/