import React, { useState } from "react";

function Account({ user }) {
  const { name, username, id, img } = user;

  return (
    <div className="card" id={id} style={{ width: "300px" }}>
      <section className="details">
        <img src={img} width={200} alt="user"></img>
        <p>Name: {name}</p>
        <p>Username: {username}</p>
      </section>
    </div>
  );
}

export default Account;
