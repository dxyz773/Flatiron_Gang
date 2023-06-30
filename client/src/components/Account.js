import React, { useState } from "react";

function Account({ updateUser }) {
  const { name, username, id } = updateUser;

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
