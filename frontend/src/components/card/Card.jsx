import React from 'react';
import propTypes from 'prop-types';
const Card = ({ children }) => {
  return <div className="rounded-lg shadow-md p-6 bg-white mx-2 my-2 max-w-md max-h-md auto">{children}</div>;
};

Card.propTypes = {
  children: propTypes.node,
}

export default Card;
