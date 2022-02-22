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

const g = new Greeter('Patchy')  // g = Greeter("Patchy")
g.greet() // g.greet() - these are the same in py and js