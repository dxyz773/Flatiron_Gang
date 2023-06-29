import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar navbar-expand-md bg-dark navbar-dark">
      <div className="container">
        <a className="navbar-brand" aria-current="page">
          <Link to={"/"} style={{ textDecoration: "none" }}>
            Flatiron Gang
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
                <Link to={"/dashboard"} style={{ textDecoration: "none" }}>
                  Fantasy Dashboard
                </Link>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <Link to={"/players"} style={{ textDecoration: "none" }}>
                  NFL Player Search
                </Link>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <Link to={"/login"} style={{ textDecoration: "none" }}>
                  User Login
                </Link>
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link active" aria-current="page">
                <Link to={"/signup"} style={{ textDecoration: "none" }}>
                  Sign up
                </Link>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
