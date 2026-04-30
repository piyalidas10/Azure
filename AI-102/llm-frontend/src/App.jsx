import React, { useState } from "react";

export default function SingleInputDualChat() {
  const [apiBase] = useState("http://172.174.48.215:8000");

  const [prompt, setPrompt] = useState("");
  const [history, setHistory] = useState([]); // full conversation log

  const [gpt5Response, setGpt5Response] = useState("");
  const [gpt4Response, setGpt4Response] = useState("");

  async function sendPrompt() {
    if (!prompt.trim()) return;

    // Add user message into history
    const newHistory = [...history, { role: "user", content: prompt }];

    const resp = await fetch(`${apiBase}/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_prompt: prompt,
        system_prompt: "You are a helpful assistant.",
        history: newHistory,
      }),
    });

    const data = await resp.json();

    const gpt5Reply = data["gpt-5"]?.response || "";
    const gpt4Reply = data["gpt-4"]?.response || "";

    // Add assistant responses to history
    const updatedHistory = [
      ...newHistory,
      { role: "assistant (GPT-5)", content: gpt5Reply },
      { role: "assistant (GPT-4)", content: gpt4Reply },
    ];

    setHistory(updatedHistory);
    setGpt5Response(gpt5Reply);
    setGpt4Response(gpt4Reply);
    setPrompt("");
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Compare GPT-5 and GPT-4</h1>

      {/* Input box */}
      <textarea
        rows="4"
        style={{ width: "100%" }}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Type your question here..."
      />
      <button onClick={sendPrompt} style={{ marginTop: "10px" }}>
        Send
      </button>

      {/* History log */}
      <div style={{ marginTop: "20px" }}>
        <h2>Conversation History</h2>
        <div style={{ whiteSpace: "pre-wrap" }}>
          {history.map((m, i) => (
            <div key={i}>
              <strong>{m.role}:</strong> {m.content}
            </div>
          ))}
        </div>
      </div>

      {/* Latest responses side by side */}
      <div style={{ display: "flex", gap: "20px", marginTop: "20px" }}>
        <div style={{ flex: 1, border: "1px solid #ccc", padding: "10px" }}>
          <h2>GPT-5 (latest)</h2>
          <div style={{ whiteSpace: "pre-wrap" }}>{gpt5Response}</div>
        </div>

        <div style={{ flex: 1, border: "1px solid #ccc", padding: "10px" }}>
          <h2>GPT-4 (latest)</h2>
          <div style={{ whiteSpace: "pre-wrap" }}>{gpt4Response}</div>
        </div>
      </div>
    </div>
  );
}
