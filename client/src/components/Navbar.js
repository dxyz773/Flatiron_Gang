import React from "react";
import { Link, NavLink, useNavigate } from "react-router-dom";

function Navbar({ updateUser, user }) {
  const navigate = useNavigate();

  function handleLogout() {
    fetch("http://127.0.0.1:5555/logout", { method: "DELETE" }).then((res) => {
      if (res.ok) {
        updateUser(null);
        navigate("/auth");
      }
    });
  }

  return (
    <nav
      className="navbar navbar-expand-md"
      style={{ backgroundColor: "#172554" }}
    >
      <div className="container">
        <a className="navbar-brand" aria-current="page">
          <Link style={{ textDecoration: "none" }} to={"/"}>
            Flatiron Gang NFL Lover
          </Link>
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
                <NavLink
                  style={{ textDecoration: "none" }}
                  className="button"
                  to="/players"
                >
                  NFL Player Database
                </NavLink>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <NavLink
                  style={{ textDecoration: "none" }}
                  className="button"
                  to="/my_likes"
                >
                  My Likes
                </NavLink>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <NavLink
                  style={{ textDecoration: "none" }}
                  className="button"
                  to="/account"
                >
                  Account
                </NavLink>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <NavLink
                  style={{ textDecoration: "none" }}
                  className="button"
                  to="/auth"
                >
                  Log In
                </NavLink>
                {user ? (
                  <div>
                    <button onClick={handleLogout} className="button">
                      Log Out
                    </button>
                    <p style={{ marginTop: "8px" }}>Hello, {user.username}</p>
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
