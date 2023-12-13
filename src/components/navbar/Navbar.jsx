import React from 'react';
import './navbar.css'
import logo from '../../assets/png/logo-no-background.png'
const Navbar = () => {
    return (
        <div className="romarr__navbar">
            <div className="romarr__navbar-logo">
                <img src={logo} alt="logo"/>

            </div>
            <div className="romarr__navbar-search">

            </div>

            <h1>games</h1>
            <h1>activity</h1>
            <h1>settings</h1>
            <h1>about</h1>
        </div>
    );
};

export default Navbar;