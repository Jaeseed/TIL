import { useState } from 'react';
import store from '../store';
export default function AddNumber () {
  const [size, setSize] = useState(0);
  const onChange = (value) => {
    setSize(value);
  }
  return(
    <div>
      <h1>Add Number</h1>
      <input type="button" value="+" onClick={function(){
        store.dispatch({type:'INCREMENT', size: size})
      }}></input>
      <input type="text" name="number" value={size} onChange={(e) => {onChange(e.target.value)}}></input>
    </div>
  )
}