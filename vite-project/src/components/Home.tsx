import React, { useState } from 'react';
import TextBoxComponent from './TextBox';
import Messages from './Messages';
import Footer from './Footer';
import { MessagesProvider } from '../contexts/MessagesContext';
import '../App.css';
import AboutUs from './Authors.tsx';
import Contacts from './Contact.tsx';
import Resources from './Resources.tsx';

function Home() {
    const selectedOption = 'reqs'
return(
    <div>
        <MessagesProvider>
            <Messages />
            <TextBoxComponent selectedOption={selectedOption} />
        </MessagesProvider>
        <Footer />
        </div>)
        
    }
        export default Home;
