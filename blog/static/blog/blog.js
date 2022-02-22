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

// CONSOLE OUTPUT: 
// blog.js:29 Hello, Patchy

class DelayedGreeter extends Greeter {
  delay = 2000

  constructor (name, delay) {
    super(name)
    if (delay !== undefined) {
      this.delay = delay
    }
  }

  greet () {
    setTimeout(
      () => {
        this.showGreeting(this.getGreeting())
      }, this.delay
    )
  }
}

const dg2 = new DelayedGreeter('Patchy 2 Seconds')
dg2.greet()

const dg1 = new DelayedGreeter('Patchy 1 Second', 1000)
dg1.greet()

// CONSOLE OUTPUT: 
// blog.js:29 Hello, Patchy 1 Second
// blog.js:29 Hello, Patchy 2 Seconds