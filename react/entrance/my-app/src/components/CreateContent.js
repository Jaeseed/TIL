import React, { Component } from 'react'

class CreateContent extends Component {
  render () {
    console.log('CreateContent render');
    return (
      <article>
        <h2>Create</h2>
        <form action="/create_process" method="post"
          // submit 버튼이 눌리면 onSubmit이벤트가 발동하는 html 고유 기능 
          onSubmit={function(e){
            e.preventDefault();
            this.props.onSubmit(
              e.target.title.value, 
              e.target.desc.value
            );
          }.bind(this)}
        >
          <p><input type="text" name="title" placeholder="title"></input></p>
          <p>
            <textarea name="desc" placeholder="description"></textarea>
          </p>
          <p>
            <input type="submit"></input>
          </p>
        </form>
      </article>
    );
  }
}

export default CreateContent