
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [log, setLog] = useState([]);

  const handleTrigger = async (endpoint) => {
    try {
      await axios.post(`http://<Your-VM-Public-IP>:5000/${endpoint}`);
      setLog(prevLog => [...prevLog, `Triggered ${endpoint} successfully.`]);
    } catch (error) {
      setLog(prevLog => [...prevLog, `Error triggering ${endpoint}: ${error.message}`]);
    }
  };

  return (
    <div className="container">
      <h1 className="header">GenAI Development Portal</h1>
      <div className="button-grid">
        <button onClick={() => handleTrigger('trigger_windsurf')}>Trigger Windsurf</button>
        <button onClick={() => handleTrigger('trigger_builder')}>Trigger Builder.io</button>
        <button onClick={() => handleTrigger('trigger_cursor')}>Trigger Cursor</button>
        <button onClick={() => handleTrigger('trigger_test')}>Trigger Test Generation</button>
        <button onClick={() => handleTrigger('trigger_pipeline')}>Trigger Azure Pipeline</button>
      </div>
      <div className="log-section">
        <h2>Process Logs / Status</h2>
        <div className="log-box">
          {log.map((entry, index) => (
            <div key={index}>{entry}</div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
