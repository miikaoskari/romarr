import React from 'react';
import propTypes from 'prop-types';
const Header = ({ children }) => {
  return (
    <div className={'flex items-center'}>
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
