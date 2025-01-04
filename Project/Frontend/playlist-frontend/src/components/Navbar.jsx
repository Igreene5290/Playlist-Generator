import { Link } from "react-router-dom";
import "../css/NavBar.css";

function NavBar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/">Playlist Generator</Link>
      </div>
      <div className="navbar-links">
        <Link to="/" className="nav-link">Home</Link>
        <Link to="/generate" className="nav-link">Generate</Link>
        <Link to="/about" className="nav-link">About</Link>      
      </div>
    </nav>
  );
}

export default NavBar;
