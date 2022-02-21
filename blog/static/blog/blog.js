// Console Logging 



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

console.time('myTimer')
console.count('counter1')
console.log('A normal log message')
console.warn('Warning: something bad might happen')
console.error('Something bad did happen!')
console.count('counter1')
console.log('All the things above took this long to happen:')
console.timeEnd('myTimer')

/* 
NOTE: The method of showing the JavaScript console depends on your browser and operating system.


- Chrome - On a Mac, it can be found under the View menu, then Developer, then JavaScript Console. On Windows, click on Tools and then Developer Tool. In the developer tools, you can click on the Console tab. You can also press the F12 key.

- Firefox - On a Mac, it can be found under the Tools menu, go to Browser Tools then Web Developer Tools. Then, select the Console tab. On Windows, click on Web Development and then Web Console. You can also press the F12 key.

- In Safari, you’ll need to enable the Develop menu. In the Safari preferences, select the Advanced tab then check Show Develop menu in the menu bar. Once you’ve done that, just choose Show JavaScript Console from the Develop menu.

*/