// src/contexts/MessagesContext.tsx
import React, { createContext, useState, useContext, ReactNode } from 'react';

interface IMessage {
    datetime: string;
    role: string;
    message: string;
    context: string;
}

interface IMessagesContext {
    messages: IMessage[];
    addMessage: (newMessage: IMessage) => void;
}

const defaultState = {
    messages: [{
        datetime: "",
        role: "Bot",
        message: "Welcome! What can I help you with today?"
    }],
    addMessage: () => { }
};

const MessagesContext = createContext<IMessagesContext>(defaultState);

export const useMessages = () => useContext(MessagesContext);

interface MessagesProviderProps {
    children: ReactNode;
}

export const MessagesProvider = ({ children }: MessagesProviderProps) => {
    // Initialize the messages state with the default welcome message
    const [messages, setMessages] = useState<IMessage[]>([{
        datetime: new Date().toISOString(), // Use the current time for the datetime
        role: "Bot",
        message: "Welcome! What can I help you with today?"
    }]);

    const addMessage = (newMessage: IMessage) => {
        setMessages(prevMessages => [...prevMessages, newMessage]);
    };

    return (
        <MessagesContext.Provider value={{ messages, addMessage }}>
            {children}
        </MessagesContext.Provider>
    );
};

