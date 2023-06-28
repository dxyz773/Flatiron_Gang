import React, { useState, useEffect } from 'react';

function Player() {
  const [players, setPlayers] = useState([]);

  // Function to fetch player data from the backend
  const fetchPlayers = async () => {
    try {
      const response = await fetch('/api/players'); // Replace '/api/players' with the actual API endpoint for fetching players
      const data = await response.json();
      setPlayers(data);
    } catch (error) {
      console.error('Error fetching players:', error);
    }
  };

  useEffect(() => {
    fetchPlayers();
  }, []);

  return (
    <div>
      <h1>Players</h1>
      <ul>
        {players.map((player) => (
          <li key={player.id}>
            <p>Name: {player.name}</p>
            <p>Position: {player.position}</p>
            <p>NFL Team: {player.nfl_team}</p>
            <p>Bye Week: {player.bye_week}</p>
            {/* Render other player properties as needed */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Player;
