import { Link } from "react-router-dom";
function Navbar() {
  return (
    <div className="container">
      <nav>
        <ul>
          <li>
            <Link to={"/"}>Flatiron Gang</Link>
          </li>
          <li>
            <Link to={"/dashboard"}>Fantasy Dashboard</Link>
          </li>
          <li>
            <Link to={"/players"}>NFL Player Search</Link>
          </li>
          <li>
            <Link to={"/signup"}>Sign up</Link>
          </li>
          <li>
            <Link to={"/login"}>Login</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Navbar;
