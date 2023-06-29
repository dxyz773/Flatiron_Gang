// import './App.css';
import React from "react";
import Navbar from "./components/Navbar";
import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import Account from "./components/Account";
import Dashboard from "./components/Dashboard";
import AllPlayers from "./components/AllPlayers";
import Player from "./components/Player";
import OneFantasyTeam from "./components/OneFantasyTeam";
import FantasyTeams from "./components/FantasyTeams";
import Game from "./components/Game";
import Auth from "./components/Auth";

import Home from "./components/Home";



function App() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    getUser()
  }, []);

  const updateUser = (user) => {
    setUser(user)
  }

  const getUser = () => {
    fetch('/check_session')
    .then(res => {
      if(res.ok){
        res.json().then(data => {
          setUser(data)
        })
      } else {
        setUser(null)
      }
    })
  }

  if (!user){
		return (
			<div className="Flatiron Gang">
				<Navbar updateUser={updateUser} user={user} />
				<Auth updateUser={updateUser} />
			</div>
		)
	}
  
  return (
    <div className="Flatiron Gang">
      <Navbar updateUser={updateUser} user={user} />
			<Routes>
        <Route path="/" element={<Home />} />
				< Route path = "/auth" element={<Auth updateUser={updateUser} />} />
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
