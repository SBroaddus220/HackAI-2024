import React from 'react';

const Authors: React.FC = () => {
    return (
        <div style={{ textAlign: 'center' }}>
            <h1>Authors</h1>
            <div style={{ display: 'flex', justifyContent: 'space-around', alignItems: 'center' }}>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Ian Stanton" />
                    <h3>Ian Stanton</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet sem nec mi elementum fermentum.</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Seth Lamancusa" />
                    <h3>Seth Lamancusa</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet sem nec mi elementum fermentum.</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Steven Broaddus" />
                    <h3>Steven Broaddus</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet sem nec mi elementum fermentum.</p>
                </div>
				<div>
                    <img src="https://via.placeholder.com/150" alt="Steven Broaddus" />
                    <h3>Joshua A'neal-Pack</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet sem nec mi elementum fermentum.</p>
                </div>
            </div>
        </div>
    );
};

export default Authors;