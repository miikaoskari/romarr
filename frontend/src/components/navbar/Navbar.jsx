import React from 'react';
import './navbar.css'
import logo from '../../assets/png/romarr-high-resolution-logo-black-transparent.png'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-solid-svg-icons'
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav>
            <div className="romarr__navbar">
                <div className="romarr__navbar-logo">
                    <img src={logo} alt="logo"/>
                </div>
                <div className="romarr__navbar-menu">
                    <ul>
                        <li><Link to={'/'}>Dashboard</Link></li>
                        <li><Link to={'/games'}>Games</Link></li>
                        <li><Link to={'/activity'}>Activity</Link></li>
                        <li><Link to={'/settings'}>Settings</Link></li>
                        <li><Link to={'/about'}>About</Link></li>
                    </ul>
                </div>
                <div className="romarr__navbar-search">

                </div>
                <div className="romarr__navbar-user">
                    <button>
                        <FontAwesomeIcon icon={faUser} className="romarr__navbar-user-icon"/>
                        User
                    </button>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;