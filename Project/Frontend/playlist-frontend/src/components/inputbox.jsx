import React, { useState } from "react";

function InputBox() {
  const [input, setInput] = useState("");
  const update = (event) => {
    setInput(event.target.value);
  };

  return (
    <div>
      <label htmlFor="minSongs"></label>
      <input
        type="number"
        id="minSongs"
        name="minSongs"
        value={input}
        onChange={update}
      />
    </div>
  );
}

export default InputBox;