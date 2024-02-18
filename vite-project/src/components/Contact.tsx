import React from 'react';

const Contacts: React.FC = () => {
    return (
        <div style={{ textAlign: 'center' }}>
            <h1>Authors Contact Information</h1>
            <div style={{ display: 'flex', justifyContent: 'space-around', alignItems: 'center' }}>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Ian Stanton" />
                    <h3>Ian Stanton</h3>
                    <p>Email: ian.stanton@example.com</p>
                    <p>Phone: 123-456-7890</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Seth Lamancusa" />
                    <h3>Seth Lamancusa</h3>
                    <p>Email: seth.lamancusa@example.com</p>
                    <p>Phone: 123-456-7890</p>
                </div>
                <div>
                    <img src="https://via.placeholder.com/150" alt="Steven Broaddus" />
                    <h3>Steven Broaddus</h3>
                    <p>Email: steven.broaddus@example.com</p>
                    <p>Phone: 123-456-7890</p>
                </div>
            </div>
        </div>
    );
};

export default Contacts;