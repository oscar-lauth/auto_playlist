import React from 'react'
import { Interface } from 'readline'



interface SongProps {
    title: string;
    artists: string[];
    album: string;
    icon: string;
  }


const Song = ({title, artists, album, icon}:SongProps) => {
  icon = "https://i.scdn.co/image/ab67616d00004851efe812ae54f0698a32ccae14"
  return (
    <div className="song-row">
        <img className="image"src={icon}/>
        <div className="detail">
            <h4 className="title">{title}</h4>
            <h6 className="artists">{artists.join(', ')}</h6>
        </div>
        <h5 className="album">{album}</h5>
    </div>
  )
}

export default Song