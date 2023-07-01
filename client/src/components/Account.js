import React, { useState } from "react";

function Account({ user }) {
  const { name, username, id } = user;

  return (
    <li className="card" id={id}>
      <section className="details">
        <p>ID: {id}</p>
        <p>Name: {name}</p>
        <p>Username: {username}</p>
      </section>
    </li>
  );
}

export default Account;
