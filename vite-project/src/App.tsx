// App.tsx
import React, { useState } from 'react';
import TextBoxComponent from './components/TextBox';
import Messages from './components/Messages';
import Footer from './components/Footer'
import { MessagesProvider } from './contexts/MessagesContext';

function App() {
<<<<<<< HEAD
    const [selectedOption, setSelectedOption] = useState<string>('');

    return (
        <div style={{
            position: 'absolute', left: '50%', top: '50%',
            transform: 'translate(-50%, -50%)'
        }} >
            <MessagesProvider>
                <Messages />
                <TextBoxComponent selectedOption={selectedOption} />
                <Footer/>
            </MessagesProvider>
        </div>
    );
=======
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
        <a href='authors.html'>Creators &emsp;&emsp;</a>
        <a href='resources.html'>Resources Utilized &emsp;&emsp;</a>
        <a href='contactus.html'>Contact Us</a>
      </footer>
    </div>
    
    
  );
>>>>>>> parent of 19d84a7 (Initial Message Addition and Better Chatbox)
}

export default App;
