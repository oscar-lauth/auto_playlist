import React from 'react'
import axios from 'axios'

const LoginButton = () => {

  return (
    <div className="login">
      <a href="http://localhost:8000/login">LOGIN</a>
      <button onClick={()=>{
        axios.post('/playlist/Granty').then(res=>{
          const playlist_id : string = res.data.id;
          axios.post('/playlist/generate/'+playlist_id).then(res=>{
            console.log("PENIS");
          })
        })
      }}>Playlist Time</button>
    </div>
  )
}

export default LoginButton