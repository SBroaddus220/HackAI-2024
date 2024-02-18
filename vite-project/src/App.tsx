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
      <footer className = 'infoFooter'>
        <a href='/authors.html'>Creators &emsp;&emsp;</a>
        <a href='/resources.html'>Resources Utilized &emsp;&emsp;</a>
        <a href='/contactus.html'>Contact Us</a>
      </footer>
    </div>
    
    
  );
}

export default App;
