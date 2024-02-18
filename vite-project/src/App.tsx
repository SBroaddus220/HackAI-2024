import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TextBoxComponent from './components/TextBox';
import Messages from './components/Messages';
import Footer from './components/Footer';
import { MessagesProvider } from './contexts/MessagesContext';
import './App.css';
import AboutUs from './components/Authors.tsx';
import Contacts from './components/Contact.tsx';
import Resources from './components/Resources.tsx';
import Home from './components/Home.tsx';

function App() {
    /*const [selectedOption, setSelectedOption] = useState<string>('');*/
    
    return (
        <Router>
            <div style={{
                position: 'absolute', left: '50%', top: '50%',
                transform: 'translate(-50%, -50%)'
            }} >
                    <Routes>
                        <Route path="/about-us" Component={AboutUs}>
                          
                        </Route>
                        <Route path="/contact" Component={Contacts}>
                          
                        </Route>
                        <Route path="/resources-used" Component={Resources}>
                        </Route>
                        <Route path="/" Component = {Home}>
                          
                        </Route>
                        </Routes>
                
                
            </div>
        </Router>
    );
}

export default App;
