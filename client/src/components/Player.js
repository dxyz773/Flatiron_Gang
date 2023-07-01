import React, { useState } from "react";
function Player({ player }) {
  const [liked, setLiked] = useState(0);
  return (
    <div className="card" key={player.id} style={{ maxWidth: 250 }}>
      <div className="card-body">
        <h6 className="card-title" style={{ fontWeight: "700" }}>
          {player.name}
        </h6>
        <img
          className="card-image-top img-fluid "
          src={player.img}
          alt={player.name}
          style={{ marginTop: "10px", marginBottom: "15px" }}
        />
        <div className="card-text" style={{ lineHeight: 1.2 }}>
          <p>{player.team}</p>
          <p>
            <span>Position: </span> {player.position}
          </p>
          <p>
            <span>#:</span> {player.number}
          </p>
          <p>
            <span>Age:</span> {player.age}
          </p>
          <p>
            <span>Bye Week:</span> {player.bye_week}
          </p>
        </div>
        <div style={{ display: "flex", gap: "10px", alignItems: "center" }}>
          <button
            className="btn btn-sm btn-primary"
            onClick={() => {
              setLiked((prev) => prev + 1);
            }}
          >
            <span role="img" aria-label="like heart">
              Like ❤️
            </span>
          </button>
          <p
            style={{ paddingTop: "12px", fontWeight: "bold", fontSize: "18px" }}
          >
            {liked}
          </p>
        </div>
      </div>
    </div>
  );
}

export default Player;
