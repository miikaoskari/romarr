import React from 'react';
import logo from '../../assets/png/romarr-high-resolution-logo-white-transparent.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import { Search } from '../index';

const Navbar = () => {


  return (
    <nav className="mt-2 bg-transparent py-1">
      <div className="container mx-auto flex items-center justify-between rounded-2xl border-x-white bg-gray-900 px-8 py-2 text-primary-light ">
        <div className="flex items-center">
          <Link to="/">
            <img className="h-auto w-32 rounded-2xl object-contain p-2 shadow-sm" src={logo} alt="logo" />
          </Link>
        </div>
        {/* Navigation Links */}
        <div className="hidden items-center space-x-4 font-semibold text-gray-300 md:flex">
          <Link to="/about" className="rounded-2xl px-3 py-2 transition-all hover:bg-gray-800">
            About
          </Link>
          <Link to="/activity" className="rounded-2xl px-3 py-2 transition-all hover:bg-gray-800">
            Activity
          </Link>
          <Link to="/games" className="rounded-2xl px-3 py-2 transition-all hover:bg-gray-800">
            Games
          </Link>
          <Link to="/settings" className="rounded-2xl px-3 py-2 transition-all hover:bg-gray-800">
            Settings
          </Link>
        </div>
        <div className="relative right-0 flex">
          <Search></Search>
        </div>
        <div className="flex items-center space-x-2 rounded-2xl px-3 py-2 text-gray-300 transition-all hover:bg-gray-800">
          <Link to="/login" className="flex items-center">
            <FontAwesomeIcon icon={faUser} size="1x" />
            <span className="ml-2">User</span>
          </Link>
        </div>
      </div>
    </nav>
  );
};
export default Navbar;
