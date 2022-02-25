
//Building React Components
/*
- Easy to write: just classes that inherit from React.Component
- At the minimum you need to implement the 'render()' method, and usually add some 'state' (although that’s not required). The 'render()' method takes no arguments, so it must vary its return value by looking at the internal state.
*/

// ClickButton Component | simple component that renders a button.

/*
When the button is clicked the text of the button will change to Clicked!. Here’s the class first, then we’ll go through what it does:
*/
class ClickButton extends React.Component {
  // Class starts by extending from React.Component - the base component
  // Then we set the state attr to an object (this is just like py dict)
  state = {
    // it has one item 'wasClicked' which stores 'clicked' status
    // of the button and defaults to false
    wasClicked: false
  }


  // Next we define a method called handleClick()
  // it will be called when button is clicked
  // name is arbritrary could be changed
  handleClick () {
    // call the setState() method - takes obj and updates given field in the component's state.
    // Only fields that are set on the passed-in object are changed, any other fields in state are unaffected
    this.setState(
      // state should only be updated using setState()
      /* because after the state is updated,
       then render() method is called automatically to update the display of the page
       If we were to try to update the state manually,
       e.g. by doing this.state.wasClicked = true
       then the page would not update. */
      {wasClicked: true}
    )
  }

  // Lastly - the render() method.
  /* its safe to read the state variables directly (but not update them). We check the status of wasClicked and
   update the buttonText appropriately.
   then create <button> element with the following properties:
   - className is rendered into the class attribute. The mt-2 class adds a margin on the top, of size 2. This is a Bootstrap specific size and if you’re curious what it actually means you can read the spacing documentation.

  - onClick is the attribute that sets the handler that’s called when the button is clicked. We’re setting it to an anonymous arrow function that in turn calls handleClick() on the component. We can’t just pass this.handleClick directly in the object as the context would be incorrect when handleClick() was called, and this would refer to the event not the component.
The last argument to React.createElement is the child we want to set on the <button>, in this case, just the buttonText.


  */
  render () {
    let buttonText

    if(this.state.wasClicked)
      buttonText = 'Clicked!'
    else
      buttonText = 'Click Me'

    return React.createElement(
      'button',
      {
        className: 'btn btn-primary mt-2',
        onClick: () => {
          this.handleClick()
        }
      },
      buttonText
    )
  }
}


class ClickButton extends React.Component {
  state = {
    wasClicked: false
  }

  handleClick () {
    this.setState(
      {wasClicked: true}
    )
  }

  render () {
    let buttonText

    if (this.state.wasClicked)
      buttonText = 'Clicked!'
    else
      buttonText = 'Click Me'

    return React.createElement(
      'button',
      {
        className: 'btn btn-primary mt-2',
        onClick: () => {
          this.handleClick()
        }
      },
      buttonText
    )
  }
}
