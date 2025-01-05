import "../css/generate.css";
import InputBox from "../components/inputbox";
import "bootstrap-icons/font/bootstrap-icons.css";
import LogIn from "../components/spotifyLogIn";

function Generate() {
  return (
    <>
      <div className="minSongsQuery">
        <h3>Choose the amount of songs required to create a playlist: </h3>
        <InputBox className="input" />
      </div>
      <div className="authenticate">
        <h3>Log in to Your Spotify Account</h3>
        <LogIn />
      </div>
    </>
  );
}

export default Generate;
