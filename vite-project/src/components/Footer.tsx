// components/Footer.tsx
import React from 'react';
import './Footer.css';

const Footer: React.FC = () => {
    return (
        <footer>
            <nav>
                <ul>
                    <li><a href="/about-us">About Us&emsp;&emsp;&emsp;&emsp;</a></li>
                    <li><a href="/contact">Contact&emsp;&emsp;&emsp;&emsp;</a></li>
                    <li><a href="/resources-used">Resources Used</a></li>
                </ul>
            </nav>
        </footer>
    );
};

export default Footer;
