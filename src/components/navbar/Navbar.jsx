import React from 'react';
import './navbar.css'
import logo from '../../assets/png/romarr-high-resolution-logo-black-transparent.png'
const Navbar = () => {
    return (
        <div className="romarr__navbar">
            <div className="romarr__navbar-logo">
                <img src={logo} alt="logo"/>
            </div>
            <div className="romarr__navbar-menu">
                <a>Dashboard</a>
                <a>Games</a>
                <a>Activity</a>
                <a>Settings</a>
                <a>About</a>
            </div>
            <div className="romarr__navbar-search">

            </div>
            <div className="romarr__navbar-user">
                <button>User</button>
            </div>
        </div>
    );
};

export default Navbar;