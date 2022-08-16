import React from 'react'

const PlaylistHeader = () => {
    const playlistIcon: string = 'https://i.ibb.co/ChGNKk9/ben.png';
    const playlistTitle: string = 'AutoPlaylist';
    const description: string = "Auto-generate a curated Spotify playlist";
    const authorText = "Created by "
    const author = "oscar";
    return (
        <div className="playlist-header">
            <img className="image" src={playlistIcon}/>
            <div className="detail">
                <h1 className="title">{playlistTitle}</h1>
                <h5 className="description">{description}</h5>
                <h5 className="authorText">{authorText}<a className="author" href="">{author}</a></h5>
                
            </div>
            
        </div>
    )
}

export default PlaylistHeader