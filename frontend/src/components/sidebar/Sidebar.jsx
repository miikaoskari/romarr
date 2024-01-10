import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../../assets/png/logo_no_text_white.png';
import { faChartLine, faGamepad, faGear, faHome, faUser } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const Sidebar = () => {
  const [selectedLink, setSelectedLink] = React.useState('/');
  const handleLinkClick = (link) => {
    setSelectedLink(link);
  };
  return (
    <div className="sticky top-0 flex h-screen flex-shrink-0 flex-col justify-between bg-gray-800 px-6 py-4 text-white">
      <div>
        <Link to="/" className={'mx-4 mb-10 mt-4'}>
          <img className="w-12" src={logo} alt="logo" />
        </Link>
        <div className={'my-2'}>
          <FontAwesomeIcon icon={faHome} className={'mx-2 text-xl text-white'} />
          <Link
            to="/about"
            className={selectedLink === '/about' ? 'mx-4 my-4 text-xl text-white' : 'mx-4 my-4 text-xl text-gray-400'}
            onClick={() => handleLinkClick('/about')}
          >
            Home
          </Link>
        </div>
        <div className={'my-2'}>
          <FontAwesomeIcon icon={faChartLine} className={'mx-2 text-xl text-white'} />
          <Link
            to="/activity"
            className={
              selectedLink === '/activity' ? 'mx-4 my-4 text-xl text-white' : 'mx-4 my-4 text-xl text-gray-400'
            }
            onClick={() => handleLinkClick('/activity')}
          >
            Activity
          </Link>
        </div>
        <div className={'my-2'}>
          <FontAwesomeIcon icon={faGamepad} className={'mx-2 text-xl text-white'} />
          <Link
            to="/games"
            className={selectedLink === '/games' ? 'mx-4 my-4 text-xl text-white' : 'mx-4 my-4 text-xl text-gray-400'}
            onClick={() => handleLinkClick('/games')}
          >
            Games
          </Link>
        </div>
        <div className={'my-2'}>
          <FontAwesomeIcon icon={faGear} className={'mx-2 text-xl text-white'} />
          <Link
            to="/settings"
            className={
              selectedLink === '/settings' ? 'mx-4 my-4 text-xl text-white' : 'mx-4 my-4 text-xl text-gray-400'
            }
            onClick={() => handleLinkClick('/settings')}
          >
            Settings
          </Link>
        </div>
      </div>
      <div>
        <FontAwesomeIcon icon={faUser} className={'mx-2 text-xl text-white'} />
        <Link
          to="/login"
          className={selectedLink === '/settings' ? 'mx-4 my-4 text-xl text-white' : 'mx-4 my-4 text-xl text-white'}
          onClick={() => handleLinkClick('/login')}
        >
          User
        </Link>
      </div>
    </div>
  );
};

export default Sidebar;
