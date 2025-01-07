import Home from "./pages/home";
import Generate from "./pages/generate";
import Loading from "./pages/loading";
import GenerateSuccess from "./pages/generatesuccess";
import Error from "./pages/error";
import NavBar from "./components/Navbar";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
      <NavBar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/generate" element={<Generate />} />
          <Route path="/loading" element={<Loading />} />
          <Route path="/generate-success" element={<GenerateSuccess />} />
          <Route path="/error" element={<Error />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
