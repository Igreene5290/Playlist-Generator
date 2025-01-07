import "../css/generate.css";
import InputBox from "../components/inputbox";
import "bootstrap-icons/font/bootstrap-icons.css";

function Generate() {
  const fetchLoading = async () => {
    try {
      // Show the loading page before starting the fetch
      console.log("about to load");
      window.location.href = "http://localhost:3000/loading";
      console.log("Loading...");

      // Wait for the fetch request to complete
      const response = await fetch(
        "http://localhost:8888/api/liked-songs-playlists",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          }
        }
      );

      // Check if response status is 200 and the result is 'success'
      const data = await response.json(); // Parse the JSON body


      if (response.status === 201 && data.result === "success") {
        // Redirect to the success page if the request was successful
        window.location.href = "http://localhost:3000/generate-success";
      } else {
        // Handle other HTTP response statuses (e.g., errors)
        console.error("Error:", response.status);
        window.location.href = "http://localhost:3000/error";
      }
    } catch (error) {
      console.error("Fetch error:", error);
      window.location.href = "http://localhost:3000/error";
    }
  };

  return (
    <>
      <div className="minSongsQuery">
        <h3>
          Choose the minimum amount of songs required to create a playlist:{" "}
        </h3>
        <div className="userInput">
          <InputBox className="input" />
          <button className="startButton" onClick={fetchLoading}>
            Go
          </button>
        </div>
      </div>
    </>
  );
}

export default Generate;
