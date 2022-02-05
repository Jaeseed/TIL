import React, {useState} from 'react'

function FunctionStateDemo() {
  const [ myMessage, setMyMessage] = useState("Hi")
  return (<>
    <h1>{myMessage}</h1>
    <button onClick={() => setMyMessage("Hello")}>Hello</button>
    <button onClick={() => setMyMessage("Bye")}>Bye</button>
  </>)
}

export default FunctionStateDemo;