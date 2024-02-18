import React from 'react';
import { useMessages } from '../contexts/MessagesContext';
import './Messages.css';

// Replace with the actual path to your default profile image in the public folder
const defaultProfilePic = '/images/defaultProfilePic.jpg';

const formatDate = (datetimeString: string) => {
    const options: Intl.DateTimeFormatOptions = {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    };
    return new Intl.DateTimeFormat('en-US', options).format(new Date(datetimeString));
};

const Messages: React.FC = () => {
    const { messages } = useMessages();

    return (
        <div className="messages-container">
            {messages.map((message, index) => (
                <div key={index} className={`${message.role}-message message`}>
                    <img src={defaultProfilePic} alt="Profile" className="profile-picture" />
                    <div className = 'messageContent'>
                        <strong>{message.role}:</strong> {message.message}
                        <div className="timestamp">{formatDate(message.datetime)}</div>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default Messages;
