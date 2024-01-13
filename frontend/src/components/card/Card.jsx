import React from 'react';
import propTypes from 'prop-types';

const Card = ({ children, image }) => {
  return (
    <div className="max-h-md auto mx-2 my-2 max-w-md rounded-lg border-2 border-gray-50 bg-white p-6 shadow-md">
      {children}
      {image && <img src={image} alt="Game"/>}
    </div>
  );
};

Card.propTypes = {
  children: propTypes.node,
  image: propTypes.string,
};

export default Card;
