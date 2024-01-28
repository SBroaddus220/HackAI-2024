import React, { useState, FormEvent } from 'react';
import '../App.css';

function TextBoxComponent() {
    const [text, setText] = useState<string>('');

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        try {
            const response = await fetch('/submit-text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });
            const responseData = await response.json();
            console.log(responseData.message);
        } catch (error) {
            console.error('Error:', error);
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
