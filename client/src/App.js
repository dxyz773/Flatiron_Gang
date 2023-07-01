// import './App.css';
import React from "react";
import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import Account from "./components/Account";
import AllPlayers from "./components/AllPlayers";
import Player from "./components/Player";
import Auth from "./components/Auth";
import Home from "./components/Home";
import Navbar from "./components/Navbar";
import MyLikes from "./components/MyLikes";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    getUser();
  }, []);

  const updateUser = (user) => {
    setUser(user);
  };

  const getUser = () => {
    fetch("http://127.0.0.1:5555/check_session").then((res) => {
      if (res.ok) {
        res.json().then((data) => {
          setUser(data);
        });
      } else {
        setUser(null);
      }
    });
  };

  if (!user) {
    return (
      <div className="Flatiron Gang">
        <Navbar updateUser={updateUser} user={user} />
        <Auth updateUser={updateUser} />
      </div>
    );
  }

  return (
    <div className="Flatiron Gang">
      <Navbar updateUser={updateUser} user={user} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/auth" element={<Auth updateUser={updateUser} />} />
        <Route path="/account" element={<Account user={user} />} />
        <Route path="/my_likes" element={<MyLikes />} />
        <Route path="/players" element={<AllPlayers />} />
        <Route path="/players/info/:name" element={<Player />} />
      </Routes>
    </div>
  );
}

export default App;
