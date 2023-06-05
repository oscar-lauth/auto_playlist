import React from 'react'
import axios from 'axios'
import Quiz from './Quiz'

interface HomeProps {
  displayName?:string;
}

const Home = ({ displayName }:HomeProps) => {
  return (
    <div className="login-page">
      <div className="summary-container">
        <h1 className="summary-title">Automate your playlist</h1>
        <p className="summary-text">Just login with Spotify and take a short quiz. We'll handle the rest.</p>
      </div>
      <div className="home-btn-container">
      {displayName ? null : <a href={process.env.REACT_APP_BACKEND_URL+"/login"} className="login-btn">LOGIN</a> }
      </div>
      { displayName ? <Quiz/> : null}
    </div>
  )
}

export default Home



