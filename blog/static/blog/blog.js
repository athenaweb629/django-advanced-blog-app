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
// Remember that since you are including the blog.js file in your template after the React scripts, you will have access to the React variable automatically.
// The /post-table/ page still won’t change as there’s one last thing we need to do: mount the component into the container. Let’s see how to do that now.
