import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <h4>Flatiron Gang Fantasy Football League Manager</h4>
      <p>Please sign up or log in to get started.</p>
      <div>
        <Link to="/signup">Sign Up</Link>
        <Link to="/login">Log In</Link>
      </div>
    </div>
  );
}

export default Home;
