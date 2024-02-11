// src/components/TextBox.tsx
import React, { useState, FormEvent } from 'react';
import { useMessages } from '../contexts/MessagesContext';

function TextBoxComponent() {
    const [text, setText] = useState<string>('');
    const { addMessage } = useMessages();
    const getServerURL = () => {
        const { protocol, hostname, port } = window.location;
        return `${protocol}//${hostname}:${port}/submit-text`;
    };

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        try {
            const response = await fetch('http://localhost:5000/submit-text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            if (response.ok) {
                const responseData = await response.json();
                console.log(responseData.message);
                setText(''); // Clear the text after successful submission
                // Add the new message to the context
                addMessage({
                    datetime: new Date().toISOString(),
                    role: 'user',
                    message: text
                });
            } else {
                console.error('Server returned an error:', response.status, response.statusText);
            }
        } catch (error: any) {
            console.error('Error:', error.message);
        }
    };


    return (
        <div className="center-container">
            <form onSubmit={handleSubmit} className="center-form">
                <input
                    type="text"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    className="center-input"
                />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default TextBoxComponent;
