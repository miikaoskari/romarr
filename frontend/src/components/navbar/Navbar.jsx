import React, { useState } from 'react';
import './navbar.css';
import logo from '../../assets/png/romarr-high-resolution-logo-black-transparent2.0.png';
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
    <nav className="py-1">
      <div className={'mx-32 flex flex-row rounded-2xl border-2 bg-white px-2 py-4 shadow-2xl'}>
        <div className="mx-2 basis-1/6">
          <Link to="/">
            <img className="w-30" src={logo} alt="logo" />
          </Link>
        </div>
        <div className="flex-auto px-2 py-1">
          <Link to="/about" className={'px-2 py-2 hover:rounded-2xl hover:bg-gray-50'}>
            About
          </Link>
          <Link to="/activity" className={'px-2 py-2 hover:rounded-2xl hover:bg-gray-50'}>
            Activity
          </Link>
          <Link to="/games" className={'px-2 py-2 hover:rounded-2xl hover:bg-gray-50'}>
            Games
          </Link>
          <Link to="/settings" className={'px-2 py-2 hover:rounded-2xl hover:bg-gray-50'}>
            Settings
          </Link>
        </div>
        <div>
          <input
            className={'rounded-2xl bg-gray-50 px-2 py-1 hover:rounded-2xl'}
            type="text"
            placeholder="Search"
            onChange={handleInputChange}
          />
          {searchResults.length > 0 && (
            <div className="dropdown-menu">
              {searchResults.map((result, index) => (
                <Search key={index} data={result} />
              ))}
            </div>
          )}
        </div>
        <div className="mx-2 origin-right px-2 py-1 hover:rounded-2xl hover:bg-gray-50">
          <Link to="/login">
            <FontAwesomeIcon icon={faUser} size="1x" className={'px-2'} />
            <span className={'px-2'}>User</span>
          </Link>
        </div>
      </div>
    </nav>
  );
};
export default Navbar;
