// src/App.tsx
import React from 'react';
import TextBoxComponent from './components/TextBox';
import Messages from './components/Messages';
import { MessagesProvider } from './contexts/MessagesContext';
import Footer from './components/Footer';
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
      <Footer />
    </div>
    
    
  );
}

export default App;
