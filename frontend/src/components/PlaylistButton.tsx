import React from 'react'

const PlaylistButton = () => {
  const btn:string = "login";
  return (
    <div className="playlist-btn-bar">
      {btn==="login" ? 
      <a href={process.env.REACT_APP_BACKEND_URL+"/login"} className="login-btn">LOGIN</a> :
      btn==="generate" ?
      <a href="" className="generate-btn">Generate</a> : 
      <a href="" className="play-btn">Play</a>
      }
    </div>
  )
}

export default PlaylistButton