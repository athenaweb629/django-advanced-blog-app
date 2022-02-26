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
    dataLoaded: true,
    data: {
      results: [
        {
          id: 15,
          tags: [
            'django', 'react'
          ],
          'hero_image': {
            'thumbnail': '/media/__sized__/hero_images/snake-419043_1920-thumbnail-100x100-70.jpg',
            'full_size': '/media/hero_images/n384_w1150_5974969766_o.jpg'
          },
          title: 'Test Post',
          slug: 'test-post',
          summary: 'A test post, created for Django/React.'
        }
      ]
    }
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

// Fetch Intro
/* https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

- fetch() is a function built into all modern browsers that preforms HTTP Requests. 

- It takes two arguments, the URL and the second is not mandetory and contains all options for the request.

Examples:
 GET         
          fetch('/api/v1/posts/')

 POST          
          fetch('/api/v1/posts/', {
            method: 'POST',
            body: data
          })
Since Fetch is promise based, a callback function to then 'then()' will need to be provided. It deals with the response, and is done by calling json().

fetch('/api/v1/posts/').then(response => {
  return response.json()
})

Is the JSON data now returned from the function? No, the json() method actually returns another Promise. Luckily, we can chain promises together so that our source code doesn’t get to unwieldy:


fetch('/api/v1/posts/').then(response => {
  return response.json()
}).then(data  => {
  // do something with data, for example
  console.log(data)
})



Like in Python, JS has try / catch / finally error handling. 


In Python - 


try:
    raise Exception("Something went wrong")
except TypeError as e:
    print("Got type error", e)
except Exception as e:
    print("Got Exception", e)
finally:
    print("This is always called")



Equivalent in JavaScript -

try {
  throw new Error('Something went wrong)
} catch(e) {
  if (e instanceof TypeError) {
    console.log('Got type error')
    console.log(e)
  } else {
    console.log('Got Exception')
    console.log(e)
  }
} finally {
  console.log('This is always called')
}



Fairly similar. Slight differences.
- 'throw' instead of 'raise'
- 'catch' innstead of 'except'
- different exception classes
- also JS doesnt have the ability to have different handlers for different exceptions. Theres one handler and one needs to check the exception class to decide how to handle it.



Handling exceptionns in promise code is a bit different. Instead of wrapping the promise in a try/catch block, we use a new method on the Promise class called 'catch()'. To this, a callback will be passed whenever an exception is raised anywhere along the promise chain.

To add exception handling to a fetch() and JSON decoding chain, catch() needs to be called at the end: 

fetch('/api/v1/posts/').then(response => {
  return response.json()
}).then(data  => {
  // do something with data, for example
  console.log(data)
}).catch(e => {
  console.error(e)
})



Here’s how we could add an exception on a non-200 response:

fetch('/api/v1/posts/').then(response => {
  if (response.status !== 200) {
    throw new Error('Invalid status from server: ' + response.statusText)
  }

  return response.json()
}).then(data  => {
  // do something with data, for example
  console.log(data)
}).catch(e => {
  console.error(e)
})




*/