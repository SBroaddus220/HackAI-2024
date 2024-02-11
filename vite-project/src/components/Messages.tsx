// src/components/Messages.tsx
import React, { useState, useEffect } from 'react';
import { useMessages } from '../contexts/MessagesContext';

const Messages: React.FC = () => {
    const { messages } = useMessages();

    return (
        <div>
            <h2>Messages:</h2>
            <ul>
                {messages.map((message, index) => (
                    <li key={index}>{message.message} - {message.datetime}</li>
                ))}
            </ul>
        </div>
    );
};

export default Messages;

