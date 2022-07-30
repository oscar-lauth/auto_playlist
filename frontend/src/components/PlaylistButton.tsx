import React from 'react'

const PlaylistButton = () => {
  const btn:string = "login";
  return (
    <div className="playlist-btn-bar">
      {btn==="login" ? 
      <a href="http://localhost:8000/login" className="login-btn">LOGIN</a> :
      btn==="generate" ?
      <a href="" className="generate-btn">Generate</a> : 
      <a href="" className="play-btn">Play</a>
      }
    </div>
  )
}

export default PlaylistButton