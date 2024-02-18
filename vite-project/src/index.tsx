import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App'; // Assuming this is your main component
import Home from './components/Home.tsx';

ReactDOM.render(
  <Router>
    <Home />
  </Router>,
  document.getElementById('root')
);