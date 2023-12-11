import React from 'react';
import './navbar.css'
import logo from '../../assets/logo.svg'
const Navbar = () => {
    return (
        <div className="romarr__navbar">
            <div className="romarr__navbar-search">
                <div className="romarr__navbar-logo">
                      <img src={logo} alt="logo"></img>
                </div>
            </div>
        </div>
    );
};

export default Navbar;