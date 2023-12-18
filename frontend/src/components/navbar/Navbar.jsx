import React, {useState, useEffect} from 'react';
import './navbar.css'
import logo from '../../assets/png/romarr-high-resolution-logo-black-transparent2.0.png'
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faUser} from '@fortawesome/free-solid-svg-icons'
import {Link} from 'react-router-dom';

const Navbar = () => {
    const [isScrolled, setIsScrolled] = useState(false)

    const handleScroll = () => {
        if (window.scrollY > 30) {
            setIsScrolled(true)
        } else {
            setIsScrolled(false)
        }
    }

    useEffect(() => {
            window.addEventListener("scroll", handleScroll);
            return () => window.removeEventListener("scroll", handleScroll)
        }
        , []);

    return (
        <nav className="py-1">
            <div className={"mx-32 flex flex-row bg-white px-2 py-4 rounded-2xl shadow-2xl border-2"}>
                <div className="basis-1/6 mx-2">
                    <Link to="/">
                        <img className="w-30" src={logo} alt="logo"/>
                    </Link>
                </div>
                <div className="flex-auto px-2 py-1">
                    <Link to="/about" className={"px-2"}>
                        About
                    </Link>
                    <Link to="/activity" className={"px-2"}>
                        Activity
                    </Link>
                    <Link to="/games" className={"px-2"}>
                        Games
                    </Link>
                    <Link to="/settings" className={"px-2"}>
                        Settings
                    </Link>
                </div>
                <div className="origin-right mx-2 py-1">
                    <FontAwesomeIcon icon={faUser} size="1x" className={"px-2"}/>
                    <span className={"px-2"}>User</span>
                </div>
            </div>
        </nav>
    );
};
export default Navbar;