// JavaScript Promises 
/* 
The purpose of promises is to provide a method of performing asynchronous code, or running code in the background. Since JavaScript doesn’t have a threading model, this accomplished with callbacks.

They do this with a consistent interface that allows a promise to be resolved (complete successfully) or (optionally) rejected (fail). In the last part of this module, we’re going to use promises when we fetch data from our API. The data fetching will happen in the background and our callback function will be executed when the data is received.

All the callbacks that are needed

Promise Construction - need atleast 2, sometimes 3 functions to implement a promise.

The first is the function that actually does the work. Rather than return a result, the worker function will call a function with the result, to “resolve” the promise. If there’s a failure in the worker function, then it might also be able to “reject” the promise.



In this example, we’ll create a lazyAdder function. It will add two numbers together. It will not return the result, but resolve it. If there is a problem with the arguments, like they are not numbers, it will reject the promise. Note that this code is not asynchronous but does have the same interface as what would be used in an asynchronous promise.
*/

const lazyAdd = function (a, b) {
  const doAdd = (resolve, reject) => {
    if (typeof a !== "number" || typeof b !== "number") {
      reject("a and b must both be numbers")
    } else {
      const sum = a + b
      resolve(sum)
    }
  }

  return new Promise(doAdd)
}