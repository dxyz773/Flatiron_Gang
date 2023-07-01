import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <img
        src="https://www.kansascity.com/latest-news/eldejx/picture267141296/alternates/FREE_1140/KCM_PhotosRaidersatChiefsOc%20(25)"
        style={{ width: 300 }}
      />
      <p>Please sign up or log in to get started.</p>
      <div className="container">
        <div className="row">
          <div className="col-auto">
            <button type="button" className="btn btn-primary">
              <Link
                style={{ textDecoration: "none", color: "white" }}
                to="/auth"
              >
                Sign Up
              </Link>
            </button>
          </div>
          <div className="col-auto">
            <button className="btn btn-primary">
              <Link
                style={{ textDecoration: "none", color: "white" }}
                to="/auth"
              >
                Login
              </Link>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
