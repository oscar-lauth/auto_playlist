import React from 'react'
import Song from './Song'

const SongList = () => {
  return (
    <ul>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown"]} album="Sleepyhead"/>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown","Beanut"]} album="Sleepyhead"/>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown"]} album="Sleepyhead"/>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown"]} album="Sleepyhead"/>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown","Beanut"]} album="Sleepyhead"/>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown"]} album="Sleepyhead"/>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown"]} album="Sleepyhead"/>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown","Beanut"]} album="Sleepyhead"/>
      <Song title="Sweet Tooth" icon="ICON" artists={["Cavetown"]} album="Sleepyhead"/>
    </ul>
  )
}

export default SongList