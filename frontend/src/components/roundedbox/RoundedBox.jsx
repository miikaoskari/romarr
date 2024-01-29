import React from 'react';
import PropTypes from 'prop-types';

const RoundedBox = ({ children }) => {
  return     <div className="mx-44 my-2 p-6 flex-grow rounded-2xl bg-gray-950  text-primary-light">{children}</div>;
};

RoundedBox.propTypes = {
  children: PropTypes.node,
};

export default RoundedBox;
