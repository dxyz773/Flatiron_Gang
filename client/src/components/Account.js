import React, { useState } from 'react';

function Account({ user }) {
  const [name, setName] = useState(user.name);
  const [username, setUsername] = useState(user.username);

  // Function to handle form submission for updating user data
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`/api/users/${user.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, username }),
      });
      const updatedUser = await response.json();
      // Handle the updated user data
    } catch (error) {
      console.error('Error updating user:', error);
    }
  };

  // Function to handle user data deletion
  const handleDelete = async () => {
    try {
      const response = await fetch(`/api/users/${user.id}`, {
        method: 'DELETE',
      });
      // Handle the user data deletion
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  return (
    <div>
      <h1>Account</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Name:
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </label>
        </div>
        <div>
          <label>
            Username:
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </label>
        </div>
        <button type="submit">Save Changes</button>
      </form>
      <button onClick={handleDelete}>Delete Account</button>
    </div>
  );
}

export default Account;
