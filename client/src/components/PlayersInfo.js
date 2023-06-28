import React, { useState, useEffect } from 'react';

function PlayersInfo() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    fetchPlayers();
  }, []);

  // Function to fetch players from the backend
  const fetchPlayers = async () => {
    try {
      const response = await fetch('/api/players'); // Replace '/api/players' with the actual API endpoint for fetching players
      const data = await response.json();
      setPlayers(data);
    } catch (error) {
      console.error('Error fetching players:', error);
    }
  };

  return (
    <div>
      <h1>Player Information</h1>
      <ul>
        {players.map((player) => (
          <li key={player.id}>
            <h2>{player.name}</h2>
            <p>Position: {player.position}</p>
            <p>NFL Team: {player.nfl_team}</p>
            <p>Bye Week: {player.bye_week}</p>
            {/* Add additional player data here */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PlayersInfo;
