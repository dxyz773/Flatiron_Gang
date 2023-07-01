import React, { useState, useEffect } from "react";
import Search from "./Search";
import Player from "./Player";

function AllPlayers() {
  const [players, setPlayers] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5555/players")
      .then((res) => res.json())
      .then((data) => setPlayers(data));
  }, []);

  function handleChange(e) {
    setSearch(e.target.value);
  }

  let searchedPlayers = players.filter((player) =>
    player.name.toLowerCase().includes(search.toLowerCase())
  );
  return (
    <div className="container">
      <div
        className="container"
        style={{
          display: "flex",
          gap: "20px",
          alignItems: "center",
          marginTop: "30px",
          marginBottom: "20px",
        }}
      >
        <h2 style={{ color: "#eff6ff" }}>Player Database</h2>
        <Search search={search} handleChange={handleChange} />
      </div>

      <div className="container fluid">
        <div className="card-group">
          {searchedPlayers.map((player) => (
            <Player key={player.id} player={player} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default AllPlayers;
