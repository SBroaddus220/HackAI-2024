// src/App.tsx
import React from 'react';
import TextBoxComponent from './components/TextBox';
import Messages from './components/Messages';
import { MessagesProvider } from './contexts/MessagesContext';

function App() {
  return (
    <div style={{
      position: 'absolute', left: '50%', top: '50%',
      transform: 'translate(-50%, -50%)' 
    }} >
      <MessagesProvider>
        <Messages />
        <TextBoxComponent />
      </MessagesProvider>
    </div>
  );
}

export default App;
