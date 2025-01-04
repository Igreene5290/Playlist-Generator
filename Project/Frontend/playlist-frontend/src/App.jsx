import Home from "./pages/home";
import Generate from "./pages/generate";
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
                </Routes>
            </main>
        </div>
  );
}



export default App;
