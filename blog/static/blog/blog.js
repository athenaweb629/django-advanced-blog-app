// Fetch & React Hooks

/* This will fetch three URLS: 

- 'api/v1/posts/' - will output valid date to the console. 

- '/' - will return a 200 status code since it exists but will fail JSON decode

- '/abadurl/' - will return a 404 and trigger exception
*/
['/api/v1/posts/', '/', '/abadurl/'].forEach(url => {
  fetch(url).then(response => {
    if (response.status !== 200) {
      throw new Error('Invalid status from server: ' + response.statusText)
    }

    return response.json()
  }).then(data => {
    // do something with data, for example
    console.log(data)
  }).catch(e => {
    console.error(e)
  })
})



// Updated for JSX
class PostRow extends React.Component {
  render () {
    const post = this.props.post

    let thumbnail

    if (post.hero_image.thumbnail) {
      thumbnail = <img src={post.hero_image.thumbnail}/>
    } else {
      thumbnail = '-'
    }

    return <tr>
      <td>{post.title}</td>
      <td>
        {thumbnail}
      </td>
      <td>{post.tags.join(', ')}</td>
      <td>{post.slug}</td>
      <td>{post.summary}</td>
      <td><a href={'/post/' + post.slug + '/'}>View</a></td>
    </tr>
  }
}

class PostTable extends React.Component {
  state = {
    dataLoaded: false,
    data: null
  }

  componentDidMount () {
    fetch('/api/v1/posts/').then(response => {
      if (response.status !== 200) {
        throw new Error('Invalid status from server: ' + response.statusText)
      }

      return response.json()
    }).then(data => {
      this.setState({
        dataLoaded: true,
        data: data
      })
    }).catch(e => {
      console.error(e)
      this.setState({
        dataLoaded: true,
        data: {
          results: []
        }
      })
    })
  }

  render () {
    let rows
    if (this.state.dataLoaded) {
      if (this.state.data.results.length) {
        rows = this.state.data.results.map(post => <PostRow post={post} key={post.id}/>)
      } else {
        rows = <tr>
          <td colSpan="6">No results found.</td>
        </tr>
      }
    } else {
      rows = <tr>
        <td colSpan="6">Loading&hellip;</td>
      </tr>
    }

    return <table className="table table-striped table-bordered mt-2">
      <thead>
      <tr>
        <th>Title</th>
        <th>Image</th>
        <th>Tags</th>
        <th>Slug</th>
        <th>Summary</th>
        <th>Link</th>
      </tr>
      </thead>
      <tbody>
      {rows}
      </tbody>
    </table>
  }
}

const domContainer = document.getElementById('react_root')
ReactDOM.render(
  React.createElement(PostTable),
  domContainer
)

// React Component Events 
/*
Throughout the lifecycle of a React component, the React library will call a few methods on it as events take place. You can implement these methods on your Component classes and hook into these events. The three most common methods are, componentDidMount(), componentDidUpdate() and componentWillUnmount().


componentDidMount
This takes no arguments, and is called right after the component is inserted into the DOM. You could use this to perform any setup of the component that’s not appropriate to do in the constructor() method. For example, we’re going to use it to start the fetch from the Post API.


componentDidUpdate
This method is called when the properties being passed to a component change. This would happen when the parent component re-renders and passes a different value for a property to the child component. For example, if the PostTable component re-renders and passes a different post property to a PostRow, then componentDidUpdate will be called on the PostRow component.
componentDidUpdate is passed three arguments:
prevProps: The props object that the component had prior to being updated, i.e. the new properties are in this.props and the ones being used before are in prevProps.


prevState: The state object that the component had prior to being updated, i.e. this.state is the new state and prevState the previous one.
snapshot: This is the result of the getSnapshotBeforeUpdate() method, which is invoked just before the rendered component is updated in the DOM. Normally you wouldn’t implement getSnapshotBeforeUpdate() as you can get the changes by comparing using prevProps and prevState. For this reason, snapshot will be null.
You can use componentDidUpdate() to check if properties you care about have changed, and then prevent extra function calls or network requests from taking place if they haven’t.
For example, we might have a PostEdit component that accepts multiple properties, including a postId. We only want to fetch the Post detail data if the postId changes, not if another property changes. We could write a componentDidUpdate() to do the check like this:
componentDidUpdate (prevProps, prevState) {
  if (prevProps.postId !== this.props.postId) {
    this.fetchPostData()
  }
}


componentWillUnmount
This is called directly before the component unmounts (is removed from the DOM). When called, the component is still attached to the DOM. You could use this method to cancel any promises that are outstanding, for example, stopping an ongoing network request.
Other Methods
There are also a few other lifecycle methods that are called, which are rarely used, such as getSnapshotBeforeUpdate(), which we already mentioned. If you find that the three methods above don’t cater to all your needs, you can read about the others at the Rarely Used Lifecycle Methods documentation.

https://reactjs.org/docs/react-component.html#rarely-used-lifecycle-methods
 */
