import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="container">
      <div
        className="card"
        style={{
          background: "#dbeafe",
          width: "300px",
          marginLeft: "auto",
          marginRight: "auto",
        }}
      >
        <div className="card-body">
          <div className="card-title">
            <p style={{ textTransform: "uppercase", fontWeight: "bold" }}>
              Please Signup or Login in to get started.
            </p>
          </div>
          <div className="card-text" style={{ display: "flex", gap: "10px" }}>
            <button type="button" className="btn btn-primary">
              <Link
                style={{ textDecoration: "none", color: "white" }}
                to="/signup"
              >
                Sign Up
              </Link>
            </button>

            <button className="btn btn-primary">
              <Link
                style={{ textDecoration: "none", color: "white" }}
                to="/login"
              >
                Login
              </Link>
            </button>
          </div>
        </div>
      </div>

      <div style={{ display: "flex", margin: "100px auto" }}>
        <img
          src="https://www.kansascity.com/latest-news/eldejx/picture267141296/alternates/FREE_1140/KCM_PhotosRaidersatChiefsOc%20(25)"
          className="img-fluid"
          alt="Patrick Mahomes and Travis Kelce after 2023 Superbowl win"
          style={{ width: 400 }}
        />

        <img
          className="img-fluid"
          src="https://ewscripps.brightspotcdn.com/dims4/default/92f4044/2147483647/strip/true/crop/7020x3949+0+0/resize/1280x720!/quality/90/?url=http%3A%2F%2Fewscripps-brightspot.s3.amazonaws.com%2F48%2F8d%2F206dcf864bc4bf425b39794fdea6%2Fyoung-2.jpg"
          alt="Panthers take Bryce Young at No. 1 overall in NFL draft"
          style={{ maxWidth: 500 }}
        />
        <img
          className="img-fluid"
          src="https://cdn.vox-cdn.com/thumbor/MkMefq_WTDZ5oHcSXFJidu_O0Fs=/0x0:3000x2000/1200x800/filters:focal(1260x760:1740x1240)/cdn.vox-cdn.com/uploads/chorus_image/image/71968001/1460609489.0.jpg"
          alt="Justin Jeferson: Philly Eagles"
          style={{ maxWidth: 400 }}
        />
      </div>
    </div>
  );
}

export default Home;
