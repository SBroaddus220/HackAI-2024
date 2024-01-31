import React, { useState, FormEvent } from 'react';
import '../App.css';

function TextBoxComponent() {
    const [text, setText] = useState<string>('');

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
            } else {
                console.error('Server returned an error:', response.status, response.statusText);
            }
        } catch (error) {
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
