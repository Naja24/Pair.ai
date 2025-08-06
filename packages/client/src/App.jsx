import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [sentiment, setSentiment] = useState("");

  const sendMessage = async () => {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    setResponse(data.response);
    setSentiment(data.sentiment);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Pair.ai Chat</h2>
      <textarea
        rows="3"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
      />
      <br />
      <button onClick={sendMessage}>Send</button>
      <div>
        <p><strong>Sentiment:</strong> {sentiment}</p>
        <p><strong>Response:</strong> {response}</p>
      </div>
    </div>
  );
}

export default App;
