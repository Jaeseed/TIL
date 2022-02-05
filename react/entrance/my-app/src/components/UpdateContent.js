import React, { Component } from 'react'

class UpdateContent extends Component {
  constructor(props){
    super(props);
    this.state = {
      id: this.props.data.id,
      title: this.props.data.title,
      desc: this.props.data.desc
    }
    this.inputFormHandler = this.inputFormHandler.bind(this)
  }
  inputFormHandler(e){
    this.setState({[e.target.name]: e.target.value});
  }
  render () {
    console.log(this.props.data);
    console.log('UpdateContent render');
    return (
      <article>
        <h2>Update</h2>
        <form action="/create_process" method="post"
          // submit 버튼이 눌리면 onSubmit이벤트가 발동하는 html 고유 기능 
          onSubmit={function(e){
            e.preventDefault();
            this.props.onSubmit(
              this.state.id,
              this.state.title, 
              this.state.desc
            );
          }.bind(this)}
        >
          <input type="hidden" name="id" value={this.state.id}></input>
          <p><input 
            type="text" 
            name="title" 
            placeholder="title"
            // value 값으로 props값을 주면 read only의 특성에서 충돌이 난다.
            value={this.state.title}
            // onChange를 써야 value 에러가 안 뜬다.
            onChange={this.inputFormHandler}
          ></input></p>
          <p>
            <textarea 
              name="desc" 
              placeholder="description" 
              value={this.state.desc}
              onChange={this.inputFormHandler}
            ></textarea>
          </p>
          <p>
            <input type="submit"></input>
          </p>
        </form>
      </article>
    );
  }
}

export default UpdateContent