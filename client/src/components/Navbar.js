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
    <nav style={{ backgroundColor: "#172554" }}>
      <div
        className="container"
        style={{ display: "flex", alignItems: "center", gap: "40px" }}
      >
        <Link style={{ textDecoration: "none" }} to={"/"}>
          Flatiron Gang NFL Lover
        </Link>

        <NavLink
          style={{ textDecoration: "none" }}
          className="button"
          to="/players"
        >
          NFL Player Database
        </NavLink>

        <NavLink
          style={{ textDecoration: "none" }}
          className="button"
          to="/my_likes"
        >
          My Likes
        </NavLink>

        <NavLink
          style={{ textDecoration: "none" }}
          className="button"
          to="/account"
        >
          Account
        </NavLink>

        <NavLink
          style={{ textDecoration: "none" }}
          className="button"
          to="/auth"
        >
          Log In
        </NavLink>
        {user ? (
          <div>
            <button onClick={handleLogout} className="btn btn-success">
              Log Out
            </button>
            <p style={{ marginTop: "8px", color: "white" }}>
              Hello, {user.username}
            </p>
          </div>
        ) : (
          ""
        )}
      </div>
    </nav>
  );
}

export default Navbar;
