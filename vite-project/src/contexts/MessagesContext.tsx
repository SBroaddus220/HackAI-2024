// src/contexts/MessagesContext.tsx
import React, { createContext, useState, useContext, ReactNode } from 'react';

interface IMessage {
    datetime: string;
    role: string;
    message: string;
}

interface IMessagesContext {
    messages: IMessage[];
    addMessage: (newMessage: IMessage) => void;
}

const defaultState = {
    messages: [],
    addMessage: () => { }
};

const MessagesContext = createContext<IMessagesContext>(defaultState);

export const useMessages = () => useContext(MessagesContext);

interface MessagesProviderProps {
    children: ReactNode;
}

export const MessagesProvider = ({ children }: MessagesProviderProps) => {
    const [messages, setMessages] = useState<IMessage[]>([]);

    const addMessage = (newMessage: IMessage) => {
        setMessages(prevMessages => [...prevMessages, newMessage]);
    };

    return (
        <MessagesContext.Provider value={{ messages, addMessage }}>
            {children}
        </MessagesContext.Provider>
    );

};
