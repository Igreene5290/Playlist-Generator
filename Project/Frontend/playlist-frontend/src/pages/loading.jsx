import { TailSpin } from "react-loading-icons";
import "../css/loading.css";

function Loading() {
  return (
    <div className="loadingSymbols">
      <TailSpin />
      <h1>Loading...</h1>
    </div>
  );
}

export default Loading;
