import { Link } from "react-router-dom";
import "../css/NavBar.css";

function NavBar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/" className="playlist-link">Playlist Generator</Link>
      </div>
      <div className="navbar-links">
        <Link to="/" className="home-link">Home</Link>
        <Link to="/generate" className="generate-link">Generate</Link>
        <Link to="/about" className="about-link">About</Link>      
      </div>
    </nav>
  );
}

export default NavBar;
