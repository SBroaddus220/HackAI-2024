// src/App.tsx
import React from 'react';
import TextBoxComponent from './components/TextBox';
import Messages from './components/Messages';
import { MessagesProvider } from './contexts/MessagesContext';
import './App.css';

function App() {
  return (
    <div style={{
      position: 'relative', top: '50%', left: '50%',
      transform: 'translate(-50%)'
    }} >
      <MessagesProvider>
        <Messages />
        <TextBoxComponent />
      </MessagesProvider>
    </div>
    
  );
}

export default App;
