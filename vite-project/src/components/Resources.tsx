import React from 'react';

const Resources: React.FC = () => {
    return (
        <div style={{ textAlign: 'center' }}>
            <h1>Resources Used</h1>
            <div style={{ display: 'flex', justifyContent: 'space-around', alignItems: 'center' }}>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Vite Logo" />
                    <h3>Vite</h3>
                    <p>A fast development server and tooling for React development.</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="React Logo" />
                    <h3>React</h3>
                    <p>A JavaScript library for building user interfaces.</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="ChromaDB Logo" />
                    <h3>ChromaDB</h3>
                    <p>A database used for storing and managing chatbot messages.</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="LangChain Logo" />
                    <h3>LangChain</h3>
                    <p>A language processing platform for building conversational AI.</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="OpenAI Logo" />
                    <h3>OpenAI API</h3>
                    <p>An API for accessing OpenAI's language models.</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Flask Logo" />
                    <h3>Flask</h3>
                    <p>A lightweight WSGI web application framework in Python.</p>
                </div>
            </div>
        </div>
    );
};

export default Resources;
