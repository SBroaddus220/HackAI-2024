import React, { useState, FormEvent } from 'react';
import '../App.css';

function TextBoxComponent() {
    const [text, setText] = useState<string>('');

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        try {


            // Send the text to the server
            console.log("Submitting text: ", text);
            const response = await fetch('/api/submit-text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            // If the response is not OK, throw an error
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Parse the JSON response
            try {
                const responseData = await response.json();
                console.log(responseData.message);
            } catch (e) {
                console.error('Error parsing JSON:', e);
            }

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
