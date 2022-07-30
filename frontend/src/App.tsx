import React from 'react';
import LoginButton from './components/LoginButton';
import PlaylistHeader from './components/PlaylistHeader';
import SongList from './components/SongList';
import PlaylistButton from './components/PlaylistButton';

function App() {
  return (
    
       <div className="App">
        <div className="playlist-container">
          <PlaylistHeader/>
          <PlaylistButton/>
          <SongList/>
      </div>
    </div>
  
  );
}

export default App;
