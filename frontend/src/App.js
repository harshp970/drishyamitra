import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/api/health`)
      .then(res => res.json())
      .then(data => setMessage(data.status));
  }, []);

  return (
    <div style={{textAlign:"center", marginTop:"100px"}}>
      <h1>Drishyamitra</h1>
      <h2>Backend Status: {message}</h2>
    </div>
  );
}

export default App;