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
    <nav className="mt-2 bg-transparent py-1">
      <div className="container mx-auto flex items-center justify-between rounded-3xl border-x-white bg-gray-900 px-8 py-2 text-primary-light ">
        <div className="flex items-center">
          <Link to="/">
            <img className="h-auto w-32 rounded-3xl object-contain p-2 shadow-sm" src={logo} alt="logo" />
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
          <input
            className="w-96 rounded-2xl bg-gray-800 px-4 py-2 pl-5 text-white outline-none transition-all hover:scale-105 hover:shadow-lg"
            type="text"
            placeholder="Search"
            onChange={handleInputChange}
          />
          {searchResults.length > 0 && (
            <div className="dropdown-menu absolute z-10 mt-1 rounded-xl bg-gray-900 text-white shadow-md">
              {searchResults.map((result, index) => (
                <Search key={index} data={result} />
              ))}
            </div>
          )}
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
