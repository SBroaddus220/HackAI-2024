// src/App.tsx
import React from 'react';
import TextBoxComponent from './components/TextBox';
import Messages from './components/Messages';
import { MessagesProvider } from './contexts/MessagesContext';

function App() {
  return (
    <div className="App">
      <MessagesProvider>
        <TextBoxComponent />
        <Messages />
      </MessagesProvider>
    </div>
  );
}

export default App;
