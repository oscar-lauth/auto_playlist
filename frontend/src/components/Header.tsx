import React from 'react'

interface HeaderProps {
    displayName?:string;
}

const Header = ({ displayName }:HeaderProps) => {

  return (
    <div className="header">
        <img src="https://cdn.discordapp.com/attachments/996867217750757477/1006051397592166410/unknown.png" alt="" />
        <h1 className="title">AUTOPLAYLIST</h1>
        {displayName ? <h3 className="user-text">Logged in as {displayName}</h3> : null}
        
    </div>
  )
}

export default Header