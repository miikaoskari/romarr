import React, { useState } from 'react';
import logo from '../../assets/png/romarr-high-resolution-logo-white-transparent.png';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import { Search } from '../index';

const Navbar = () => {
  const [query, setQuery] = useState('');
  const [timerId, setTimerId] = useState(null);
  const [searchResults, setSearchResults] = useState([]);

  const fetchGames = async () => {
    const response = await fetch(`http://localhost:8000/search/${query}`);
    const data = await response.json();
    console.log(data);
    setSearchResults(data);
    console.log(searchResults);
  };
  const handleInputChange = (event) => {
    clearTimeout(timerId);
    setQuery(event.target.value);
    const timer = setTimeout(fetchGames, 500);
    setTimerId(timer);
  };

  return (
    <nav className="py-1 mt-2 bg-transparent">
    <div className="container mx-auto flex items-center justify-between py-2 px-8 rounded-3xl text-primary-light bg-gray-900 border-x-white ">
        <div className="flex items-center">
            <Link to="/">
                <img className="w-32 h-auto object-contain p-2 rounded-3xl shadow-sm" src={logo} alt="logo" />
            </Link>
        </div>

        {/* Navigation Links */}
        <div className="hidden md:flex items-center space-x-4 font-semibold text-gray-300">
            <Link to="/about" className="px-3 py-2 rounded-2xl hover:bg-gray-800 transition-all">About</Link>
            <Link to="/activity" className="px-3 py-2 rounded-2xl hover:bg-gray-800 transition-all">Activity</Link>
            <Link to="/games" className="px-3 py-2 rounded-2xl hover:bg-gray-800 transition-all">Games</Link>
            <Link to="/settings" className="px-3 py-2 rounded-2xl hover:bg-gray-800 transition-all">Settings</Link>
        </div>

        <div className="flex right-0 relative">
            <input
                className="rounded-2xl w-96 bg-gray-800 px-4 py-2 pl-5 outline-none hover:scale-105 hover:shadow-lg transition-all text-white"
                type="text"
                placeholder="Search"
                onChange={handleInputChange}
            />
            {searchResults.length > 0 && (
                <div className="dropdown-menu absolute bg-gray-900 shadow-md mt-1 rounded-xl z-10 text-white">
                    {searchResults.map((result, index) => (
                        <Search key={index} data={result} />
                    ))}
                </div>
            )}
        </div>

        <div className="flex items-center space-x-2 hover:bg-gray-800 rounded-2xl px-3 py-2 transition-all text-gray-300">
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
