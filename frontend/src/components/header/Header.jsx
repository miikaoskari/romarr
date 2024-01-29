import React from 'react';
import propTypes from 'prop-types';
const Header = ({ children }) => {
  return (
    <div className={'flex items-center bg-gray-900 p-1 rounded-3xl m-1 right-0 w-max bottom-0 mb-2 fixed hover:p-5 transition-all text-white'}>
      {React.Children.map(children, (child) => (
        <div className={'flex-1'}>{child}</div>
      ))}
    </div>
  );
};

Header.propTypes = {
  children: propTypes.node,
};

export default Header;
