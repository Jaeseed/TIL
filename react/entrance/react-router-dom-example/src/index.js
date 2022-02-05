import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter, Route, Routes, NavLink} from 'react-router-dom'

function Home() {
  return (
    <div>
      <h2>Home</h2>
      Home...
    </div>
  )
}

function Topics() {
  return (
    <div>
      <h2>Topics</h2>
      <ul>
        <li><NavLink to="/topics/1">HTML</NavLink></li>
        <li><NavLink to="/topics/2">JS</NavLink></li>
        <li><NavLink to="/topics/3">REACT</NavLink></li>
      </ul>
      <Routes>
        <Route path="/topics/1">
          HTML is...
        </Route>
        <Route path="/topics/2">
          JS is...
        </Route>
        <Route path="/topics/3">
          REACT is...
        </Route>
      </Routes>
    </div>
  )
}

function Contact() {
  return (
    <div>
      <h2>Contact</h2>
      Contact...
    </div>
  )
}


function App() {
  return (
    <div>
      <h1>React Router DOM example</h1>
      {/* 페이지 로딩이 들어감 */}
      {/* <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/topics">Topics</a></li>
        <li><a href="/contact">contact</a></li>
      </ul> */}
      {/* 페이지 로딩 없이 SPA로 진행 */}
      <ul>
        <li><NavLink to="/">Home</NavLink></li>
        <li><NavLink to="/topics/*">Topics</NavLink></li>
        <li><NavLink to="/contact">contact</NavLink></li>
      </ul>
      <Routes>
        <Route exact path="/" element={<Home/>}/>
        <Route path="/topics/*" element={<Topics/>}/>
        <Route path="/contact" element={<Contact/>}/>
      </Routes>
    </div>
  )
}

ReactDOM.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
