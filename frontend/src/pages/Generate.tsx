import React, { useState } from 'react'
import axios from 'axios'

interface GenerateProps {
    params:string[];
}

const Generate = ({ params }:GenerateProps) => {
    const playlistName:string="NON";
    const [playlistID,setPlaylistID] = useState("");
  return (
    <div className="generate-container">
    <button className="generate-btn" onClick={()=>{
        axios.post('/playlist/'+playlistName).then(res=>{
            setPlaylistID(res.data.id);
            const playlistLink:string = res.data.external_urls.spotify;
            axios.post('/playlist/generate/'+playlistID).then(res=>{
                console.log("GENERATED:"+playlistLink);
                console.log(params);
            })
        })
    }}>
        GENERATE
    </button>
    {playlistID!=="" ?  <iframe className="playlist-preview" src={"https://open.spotify.com/embed/playlist/"+playlistID+"?utm_source=generator"} width="100%" height="380" frameBorder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>:null}
    </div>
  )
}

export default Generate
