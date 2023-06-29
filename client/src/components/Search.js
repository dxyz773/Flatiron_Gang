function Search({ search, handleChange }) {
  return (
    <div>
      <input type="text" value={search} onChange={(e) => handleChange(e)} />
    </div>
  );
}

export default Search;
