import React from "react";

function Search({ search, handleChange }) {
  return (
    <form style={{ width: "500px" }}>
      <div className="form-floating">
        <input
          className="form-control form-control-sm"
          type="text"
          value={search}
          onChange={(e) => handleChange(e)}
          placeholder="Search here"
        />
        <label className="form-label">NFL Player Search</label>
      </div>
    </form>
  );
}

export default Search;
