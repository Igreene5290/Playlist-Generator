import "../css/home.css";

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
      <a href="./generate">
        <button className="buttons">Generate</button>
      </a>
    </div>
  );
}

export default Home;
