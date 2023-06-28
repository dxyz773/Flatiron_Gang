import React, { useState, useEffect } from 'react';

function Game() {
  const [games, setGames] = useState([]);

  // Function to fetch game data from the backend
  const fetchGames = async () => {
    try {
      const response = await fetch('/api/games'); // Replace '/api/games' with the actual API endpoint for fetching games
      const data = await response.json();
      setGames(data);
    } catch (error) {
      console.error('Error fetching games:', error);
    }
  };

  useEffect(() => {
    fetchGames();
  }, []);

  return (
    <div>
      <h1>Games</h1>
      <ul>
        {games.map((game) => (
          <li key={game.id}>
            <p>Game ID: {game.id}</p>
            <p>Team 1 ID: {game.team_1_id}</p>
            <p>Team 2 ID: {game.team_2_id}</p>
            <p>Team 1 Score: {game.team_1_score}</p>
            <p>Team 2 Score: {game.team_2_score}</p>
            <p>Winner ID: {game.winner_id}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Game;
