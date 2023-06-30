import React from "react";
function Player({ player, handleDelete }) {
  return (
    <div>
      <ul>
        <li key={player.id}>
          <p>Name: {player.name}</p>
          <p>Position: {player.position}</p>
          <p>NFL Team: {player.nfl_team}</p>
          <p>Bye Week: {player.bye_week}</p>
          <button onClick={() => handleDelete(player.id)}></button>
          {/* Render other player properties as needed */}
        </li>
      </ul>
    </div>
  );
}

export default Player;
