// TextBox.tsx
import React, { useState, FormEvent } from 'react';
import { useMessages } from '../contexts/MessagesContext';

interface TextBoxProps {
    selectedOption: string; // Prop to hold the selected value from the dropdown
}

const TextBoxComponent: React.FC<TextBoxProps> = ({ selectedOption }) => {
    const [text, setText] = useState<string>('');
    const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
    const { addMessage } = useMessages();
    const textareaRef = useRef<HTMLTextAreaElement>(null);

    useEffect(() => {
        if (textareaRef.current) {
            // Dynamically adjust the height to fit the content
            textareaRef.current.style.height = 'auto'; // Reset height to recalculate
            textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
        }
    }, [text]);
    const [context, setContext] = useState<string>('reqs');
        const handleSelection = (event: React.ChangeEvent<HTMLSelectElement>) => {
            setContext(event.target.value);
        };
    


    const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setIsSubmitting(true);
        try {
            const response = await fetch('/api/submit-text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text, context }), // Use selectedOption as the context
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const responseData = await response.json();
            setText(''); // Clear input field
            // Add user message with context
            addMessage({
                datetime: new Date().toISOString(),
                role: 'User',
                message: text,
                context: selectedOption
            });
            // Optionally handle bot response
            if (responseData.response) {
                addMessage({
                    datetime: new Date().toISOString(),
                    role: 'Bot',
                    message: responseData.response.message,
                    context: 'spec'
                });
            }
        } catch (error) {
            console.error('Error:', error);
        } finally {
            setIsSubmitting(false); // Re-enable the button after submission
        }
    };

    return (
        <div className="center-container">
            <form onSubmit={handleSubmit} className="center-form">
                <textarea
                    ref={textareaRef}
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    className="center-input"
                    style={{
                        resize: 'none', // Allow vertical resizing only
                        width: '200%', // This will now effectively be 80% of the viewport width due to #root's max-width
                        minWidth: '100px', // Minimum width
                        minHeight: '50px', // Minimum height
                        paddingLeft: '1px',
                        paddingRight: '1px',
                        overflowY: 'auto' // Automatically add scrollbar when needed
                    }}
                    
                    rows={1} // Start with a single row
                />
                <button type="submit" disabled={isSubmitting}>Submit</button>
                {isSubmitting && <div className="spinner"></div>} {/* Conditionally render the spinner */}
            </form>
            <select onChange={handleSelection}>
                <option value="reqs">Major Requirements for CSE</option>
                <option value="specs">Specialization Option</option>
            </select>
        </div>
    );
};

export default TextBoxComponent;
