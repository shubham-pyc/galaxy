import React from 'react';
import './App.css';
import NetworkGraph from './components/NetworkGraph';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Network Visualization</h1>
      </header>
      <main>
        <NetworkGraph />
      </main>
    </div>
  );
}

export default App;
