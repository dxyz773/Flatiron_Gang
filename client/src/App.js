// import './App.css';
import React from "react";
import Navbar from "./components/Navbar";
import { Routes, Route } from "react-router-dom";

import Account from "./components/Account";
import Dashboard from "./components/Dashboard";
import AllPlayers from "./components/AllPlayers";
import Player from "./components/Player";
import OneFantasyTeam from "./components/OneFantasyTeam";
import FantasyTeams from "./components/FantasyTeams";
import Game from "./components/Game";
import Login from "./components/Login";
import Signup from "./components/Signup";
import Home from "./components/Home";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/account" element={<Account />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/fantasy_teams" element={<FantasyTeams />} />
        <Route path="/fantasy_teams/:name" element={<OneFantasyTeam />} />
        <Route path="/players" element={<AllPlayers />} />
        <Route path="/players/info/:name" element={<Player />} />
        <Route path="/fantasy_game" element={<Game />} />
      </Routes>
    </div>
  );
}

export default App;
