import React from "react";
function Player({ player }) {
  return (
    <div className="card" style={{ width: 240 }} key={player.id}>
      <div className="card-body">
        <h4 className="card-title">{player.name}</h4>
        <img className="card-image-top" src={player.img} />
        <div className="card-text">
          <p>NFL Team: {player.team}</p>
          <p>Position: {player.position}</p>
          <p>#: {player.number}</p>
          <p>Age: {player.age}</p>
          <p>Bye Week: {player.bye_week}</p>
        </div>
      </div>
      {/* Render other player properties as needed */}
    </div>
  );
}

export default Player;
