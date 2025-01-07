import "../css/home.css";
import LogInButton from "../components/spotifyLogIn";

function Home() {
  return (
    <div className="home">
      <h1>Welcome</h1>
      <div className="headers">
        <h2 className="likedHeader">Liked Songs => Playlists</h2>
        <h2>Generate Playlist From Genre/Mood</h2>
      </div>
      <div className="subText">
        <p className="likedSubText">
          Search through all the songs in your liked songs playlist and sort
          them into playlists based on their genre. Choose the amount of songs
          required for a playlist to be created.
        </p>
      </div>
      <div className="authenticate">
        <h3>Log in to Your Spotify Account</h3>
        <LogInButton />
      </div>
    </div>
  );
}

export default Home;
