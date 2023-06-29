import React, { useState } from 'react';

function UserLogin() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  // Function to handle form submission for user login
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });
      // Handle the response after user login
    } catch (error) {
      console.error('Error logging in:', error);
    }
  };

  return (
    <div>
      <h1>User Login</h1>
      <form onSubmit={handleSubmit}>
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
        <div>
          <label>
            Password:
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </label>
        </div>
        <button type="submit">Log In</button>
      </form>
    </div>
  );
}

export default UserLogin;
