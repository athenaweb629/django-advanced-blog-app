// JavaScript Classes - Inheritance, Attributes, and Arrow Functions

// Note - Unlike Python classes, they can only inherit from one super class

// The constructor method is called 'constructor', and is the equivalent of Python’s '__init__'. 

// When instantiating a class, you must use the new keywords, you can’t just “call” the class as you do in Python.

// To access the current object from within the class, the keyword 'this' is used. It’s the equivalent of self in Python, but is implicit, i.e. this is not passed to every method like self is.

// inheritance is denoted with the 'extends' keyword.

class Greeter {
  // def __init__(self, name='no name'):
  constructor (name) {
    this.name = name
  }

  getGreeting () {
    if (this.name === undefined) {
      return 'Hello, no name'
    }

    return 'Hello, ' + this.name
  }
  // return f'Hello, {self.name}'

  showGreeting (greetingMessage) {
    console.log(greetingMessage)
  }
  // The main “entrypoint” to the class - greet()
  greet () {
    this.showGreeting(this.getGreeting())
  }
}

const g = new Greeter('Patchy')  // g = Greeter("Patchy")
g.greet() // g.greet() - these are the same in py and js



class DelayedGreeter extends Greeter {

} // 'extends' in js is equiv to 'DelayedGreeter(Greeter)' in py


// Let’s override the constructor, so as well as providing a name, we can also provide an optional delay. We’ll make use of super(), a special function that calls the method in which it’s used on the superclass. It’s similar to the super() method in Python, but not as explicit in its behavior:

class DelayedGreeter extends Greeter {
  constructor (name, delay) {
    super(name)
    if (delay !== undefined) {
      this.delay = delay
    }
  }
}


// Here, super(name) calls the constructor() method on Greeter, with the name argument. We then set this.delay to the delay argument, if it’s passed in.
// If it’s not passed in, then what will delay be? Currently, it’s undefined, but we can fix that by setting an attribute. Like in Python, attributes are just set in the class body. Here, we’ll set delay to a default of 2000, or 2 seconds:


class DelayedGreeter extends Greeter {
  delay = 2000

  constructor (name, delay) {
    super(name)
    if (delay !== undefined) {
      this.delay = delay
    }
  }

// Finally we’ll override the greet() method to use setTimeout() and greet after a delay.

  class DelayedGreeter extends Greeter {
  // other methods/attribute omitted

  greet () {
    setTimeout(
      () => {
        this.showGreeting(this.getGreeting())
      }, this.delay
    )
  }
}


// Here we’ve used an arrow function, instead of a function defined with the function keyword, like this:

setTimeout(
  function() {
    this.showGreeting(this.getGreeting())
  }, this.delay
)





// When using “traditional” functions (arrow functions are relatively new to JavaScript), the context in which the function executes changes. The upshot is that this, inside a function, no longer refers to the class instance. Instead it refers to the function itself. If we call this.showGreeting() it will fail as the function doesn’t have a showGreeting() method.
// Using an arrow function avoids this problem, and the function executes in the context you expect with 'this' referring to the class instance. All browsers released in the last few years support arrow function so you should prefer to use them unless you have a good reason not to.