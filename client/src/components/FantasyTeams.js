import React, { useState, useEffect } from 'react';

function FantasyTeams() {
  const [teams, setTeams] = useState([]);

  // Function to fetch teams from the backend
  const fetchTeams = async () => {
    try {
      const response = await fetch('/api/teams'); // Replace '/api/teams' with the actual API endpoint for fetching teams
      const data = await response.json();
      setTeams(data);
    } catch (error) {
      console.error('Error fetching teams:', error);
    }
  };

  // Function to create a new team
  const createTeam = async (teamData) => {
    try {
      const response = await fetch('/api/teams', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(teamData),
      });
      const newTeam = await response.json();
      setTeams([...teams, newTeam]);
    } catch (error) {
      console.error('Error creating team:', error);
    }
  };

  // Function to update an existing team
  const updateTeam = async (teamId, teamData) => {
    try {
      const response = await fetch(`/api/teams/${teamId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(teamData),
      });
      const updatedTeam = await response.json();
      const updatedTeams = teams.map((team) =>
        team.id === teamId ? updatedTeam : team
      );
      setTeams(updatedTeams);
    } catch (error) {
      console.error('Error updating team:', error);
    }
  };

  useEffect(() => {
    fetchTeams();
  }, []);

  return (
    <div>
      <h1>Fantasy Teams</h1>
      <ul>
        {teams.map((team) => (
          <li key={team.id}>{team.name}</li>
        ))}
      </ul>
      <button onClick={() => createTeam({ name: 'New Team' })}>
        Create Team
      </button>
      <button
        onClick={() => updateTeam(1, { name: 'Updated Team' })} // Replace 1 with the ID of the team you want to update
      >
        Update Team
      </button>
    </div>
  );
}

export default FantasyTeams;
