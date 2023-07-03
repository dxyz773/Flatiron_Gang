import React, { useState } from "react";

function MyLikes({ user }) {
  const [myLikes, setMyLikes] = useState([]);
  function handleClick() {
    fetch(`http://127.0.0.1:5555/fans/${user.id}`).then((res) =>
      res.json().then((data) => setMyLikes(data.likes))
    );
  }
  return (
    <div className="container">
      <button onClick={() => handleClick()} className="btn btn-success">
        View likes
      </button>
      <ul style={{ display: "flex", gap: "20px" }}>
        {myLikes.map((one) => (
          <li key={one.id}>
            <div className="card" style={{ width: "250px" }}>
              <div className="card-body">
                <h6 className="card-title" style={{ fontWeight: "700" }}>
                  {one.player.name}
                </h6>
                <img
                  className="card-image-top img-fluid "
                  src={one.player.img}
                  alt={one.player.name}
                  style={{ marginTop: "10px", marginBottom: "15px" }}
                />
                <div className="card-text" style={{ lineHeight: 1.2 }}>
                  <p>{one.player.team}</p>
                  <p>
                    <span>Position: </span>
                    {one.player.position}
                  </p>
                  <p>
                    <span>#:</span> {one.player.number}
                  </p>
                  <p>
                    <span>Age:</span> {one.player.age}
                  </p>
                  <p>
                    <span>Bye Week:</span> {one.player.bye_week}
                  </p>
                </div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MyLikes;
