import { useState } from "react"
import store from "../store";

export default function DisplayNumber (props) {
  const [number, setNumber] = useState(store.getState().number);
  store.subscribe(function(){
    setNumber(store.getState().number)
  })
  return(
    <div>
      <h1>DisplayNumber</h1>
      <input type="text" value={number} readOnly></input>
    </div>
  )
}