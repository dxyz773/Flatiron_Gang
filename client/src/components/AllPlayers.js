import React, { useState, useEffect } from "react";
import Search from "./Search";
import Player from "./Player";

function AllPlayers() {
  const [players, setPlayers] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetchPlayers();
  }, []);

  // Function to fetch players from the backend
  const fetchPlayers = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5555/players");
      const data = await response.json();
      setPlayers(data);
    } catch (error) {
      console.error("Error fetching players:", error);
    }
  };
  console.log(search);

  function handleChange(e) {
    setSearch(e.target.value);
  }
  let searchedPlayers = players.filter((player) =>
    player.name.toLowerCase().includes(search.toLowerCase())
  );
  return (
    <div>
      <Search search={search} handleChange={handleChange} />
      <h1>Player Information</h1>
      <ul>
        {searchedPlayers.map((player) => (
          <Player key={player.id} player={player} />
        ))}
      </ul>
    </div>
  );
}

export default AllPlayers;