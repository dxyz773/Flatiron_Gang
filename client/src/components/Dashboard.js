import React, { useState, useEffect } from 'react';

function Dashboard({ userId }) {
  const [team, setTeam] = useState(null);

  useEffect(() => {
    fetchUserTeam();
  }, []);

  // Function to fetch the team tied to a specific user from the backend
  const fetchUserTeam = async () => {
    try {
      const response = await fetch(`/api/users/${userId}/team`); // Replace '/api/users/:userId/team' with the actual API endpoint for fetching the user's team
      const data = await response.json();
      setTeam(data);
    } catch (error) {
      console.error('Error fetching user team:', error);
    }
  };

  if (!team) {
    return <div>Loading team...</div>;
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <h2>Team: {team.team_name}</h2>
      {/* Display additional team information */}
    </div>
  );
}

export default Dashboard;
