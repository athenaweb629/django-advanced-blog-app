// JSX Intro

class ClickButton extends React.Component {
  state = {
    wasClicked: false
  }

  handleClick () {
    this.setState(
      {wasClicked: true}
    )
  }


  // Updated to return JSX instead of using React.createElement()
   render () {
    let buttonText

    if (this.state.wasClicked)
      buttonText = 'Clicked!'
    else
      buttonText = 'Click Me'

    return <button
      className="btn btn-primary mt-2"
      onClick={
        () => {
          this.handleClick()
        }
      }
    >
      {buttonText}
    </button>
  }
// Mounting a Component

const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(ClickButton),
  domContainer
)
// side note - button disables after 2 clicks
