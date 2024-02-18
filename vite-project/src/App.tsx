// App.tsx
import React, { useState } from 'react';
import TextBoxComponent from './components/TextBox';
import Messages from './components/Messages';
import Footer from './components/Footer'
import { MessagesProvider } from './contexts/MessagesContext';

function App() {
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
}

export default App;
