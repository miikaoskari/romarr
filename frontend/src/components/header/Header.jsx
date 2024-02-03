import React from 'react';
import propTypes from 'prop-types';
const Header = ({ children }) => {
  return (
    <div
      className={
        'fixed bottom-0 right-0 m-1 mb-2 flex w-max items-center rounded-3xl bg-gray-900 p-1 text-white transition-all hover:p-5'
      }
    >
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
