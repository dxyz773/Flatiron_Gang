import React from "react";
import { Link, NavLink, useNavigate } from "react-router-dom";

function Navbar({ updateUser, user }) {
  const navigate = useNavigate();

  function handleLogout() {
    fetch("/logout").then((res) => {
      if (res.ok) {
        updateUser(null);
        navigate("/auth");
      }
    });
  }

  return (
    <nav className="navbar navbar-expand-md bg-dark navbar-dark">
      <div className="container">
        <a className="navbar-brand" aria-current="page">
          <Link to={"/"}>Flatiron Gang</Link>
        </a>
        <button
          className="navbar-toggler"
          data-bs-toggle="collapse"
          data-bs-target="#nav"
          aria-controls="nav"
          aria-label="Expand Navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="nav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <NavLink className="button" to="/dashboard" end>
                  Fantasy Dashboard
                </NavLink>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <NavLink className="button" to="/players">
                  NFL Player Search
                </NavLink>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <NavLink className="button" to="/account">
                  Account
                </NavLink>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <NavLink className="button" to="/auth">
                  Log In
                </NavLink>
                {user ? (
                  <div>
                    <button onClick={handleLogout} className="button">
                      Log Out
                    </button>
                    <p style={{ "margin-top": "8px" }}>
                      Hello, {user.username}
                    </p>
                  </div>
                ) : (
                  ""
                )}
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
