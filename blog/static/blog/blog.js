// JavaScript Classes 

// Note - Unlike Python classes, they can only inherit from one super class

// The constructor method is called 'constructor', and is the equivalent of Python’s '__init__'. 

// When instantiating a class, you must use the new keywords, you can’t just “call” the class as you do in Python.

// To access the current object from within the class, the keyword 'this' is used. It’s the equivalent of self in Python, but is implicit, i.e. this is not passed to every method like self is.

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

// The other methods are: getGreeting(), which will build the greeting string based on the name that was passed to the constructor; and showGreeting(), which is just a wrapper around console.log(). It could be overridden in a child class to output the message in another way (maybe in an alert()). Note that the methods don’t need to be preceded with function or use the => operator, the interpreter can deduce that they’re methods because they have parentheses at the end of their identifier.

// Here’s how the class is instantiated and used:

const g = new Greeter('Patchy')
g.greet()

// This will output Hello, Patchy to the console, by calling greet() which calls showGreeting() with the result of getGreeting().