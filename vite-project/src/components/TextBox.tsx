import React, { useState, FormEvent } from 'react';
import { useMessages } from '../contexts/MessagesContext';

function TextBoxComponent() {
    const [text, setText] = useState<string>('');
    const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
    const { addMessage } = useMessages();

    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setIsSubmitting(true);
        try {
            const response = await fetch('/api/submit-text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const responseData = await response.json();
            setText(''); // Clear input field
            // Add user message
            addMessage({
                datetime: new Date().toISOString(),
                role: 'User',
                message: text
            });
            // Optionally handle bot response
            if (responseData.response) {
                addMessage({
                    datetime: new Date().toISOString(),
                    role: 'Bot',
                    message: responseData.response.message
                });
            }
        } catch (error) {
            console.error('Error:', error);
        } finally {
            setIsSubmitting(false); // Re-enable the button
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
                <button type="submit" disabled={isSubmitting}>Submit</button>
                {isSubmitting && <div className="spinner"></div>} {/* Conditionally render the spinner */}
            </form>
        </div>
    );
}

export default TextBoxComponent;
