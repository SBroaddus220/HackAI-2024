import React from 'react';
import { useMessages } from '../contexts/MessagesContext';
import './Messages.css';

const Messages: React.FC = () => {
    const { messages } = useMessages();

    return (
        <div className="messages-container">
            {messages.map((message, index) => (
                <div key={index} className={`${message.role}-message`}>
                    {message.role}: {message.message}
                    <div className="timestamp">{message.datetime}</div>
                </div>
            ))}
        </div>
    );
};

export default Messages;