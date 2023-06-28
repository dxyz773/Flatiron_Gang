import React, { useState, useEffect } from 'react';

function OneFantasyTeam({ teamId }) {
  const [team, setTeam] = useState(null);

  useEffect(() => {
    fetchTeam();
  }, []);

  // Function to fetch a single team from the backend
  const fetchTeam = async () => {
    try {
      const response = await fetch(`/api/teams/${teamId}`); // Replace '/api/teams/:teamId' with the actual API endpoint for fetching a team
      const data = await response.json();
      setTeam(data);
    } catch (error) {
      console.error('Error fetching team:', error);
    }
  };

  if (!team) {
    return <div>Loading team...</div>;
  }

  return (
    <div>
      <h1>{team.team_name}</h1>
      {/* Display additional team information */}
    </div>
  );
}

export default OneFantasyTeam;
