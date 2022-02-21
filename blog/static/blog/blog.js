function sayHello(name) {
  if (name === undefined) {
      console.log('Hello, no name')
  } else {
       console.log('Hello, ' + name)
  }
}

const name = 'Your Name'  // Put your name here

console.log('Before setTimeout')

setTimeout(() => {
    sayHello(name)
  }, 2000
)

console.log('After setTimeout')


/*
the anonymous function has accessed the name variable in the outer scope. Also pay attention to the order in which the messages are printed to the console. The execution doesn’t stop when setTimeout() is called. It continues on and the After setTimeout message is displayed immediately. Two seconds later, the sayHello() function is called and the greeting is displayed.
*/