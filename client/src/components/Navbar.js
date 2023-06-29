import { Link, NavLink, useNavigate } from "react-router-dom";

function Navbar({ updateUser, user }) {
	const navigate = useNavigate();

	function handleLogout() {
		fetch("/logout").then((res) => {
			if (res.ok){
				updateUser(null);
				navigate("/auth");
			}
		});
	}

	return (
    <header>
        <h1>
          <Link to={"/"}>{"//"}Flatiron Gang</Link>
        </h1>
			<div className="container">
          <NavLink className="button" to="/dashboard" end>
            Fantasy Dashboard
          </NavLink>
          <NavLink className="button" to="/players">
            NFL Player Search
          </NavLink>
          <NavLink className="button" to="/auth">
            Log In
          </NavLink>
          { user ? 
            (<>
              <button onClick={handleLogout} className="button">
                Log Out
              </button>
              <p style={{'margin-top': '8px'}}>Hello, {user.username}</p>
            </>) : 
            ''
          }		
			</div>
    </header>
	);


}

export default Navbar;