const framework = 'Django'
const language = 'Python'
alert(framework + ' is written in ' + language)

  /* Note - Lines in javascript can be terminated with a semi colon. concatenated works the same as it does in python.
   */ 

  const name = 'Ben'
let benCount = 0
if (name === 'Ben') {
    benCount = 1
}

alert('There is ' + benCount + ' Ben')
/*
Contional statements - the 'IF' statment must have parentheses around it. For a single line 'if' statement, curly braces are not required, but sometimes it can be preferable to always use them to be very clear which parts of the code are inside the if body.
*/

/* 
Notice that we’re using triple-equals (===) to compare the variables in the condition. Using === means that the types of the items being compared are taken into comparison. For example, in JavaScript we could compare the string '1' and number 1 with ==. This would evaluate to true, as JavaScript coerces them to the same type and then compares. With === type coercion doesn’t take place, so '1' === 1 is false.
*/