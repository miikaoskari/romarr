import React from 'react';
import propTypes from 'prop-types';

const Card = ({ children, image, header, content }) => {
  return (
    <div className="max-h-md auto mx-2 my-2 max-w-md rounded-3xl border-2 border-gray-800 bg-gray-800 p-6 shadow-md">
      {children}
      {image && <img src={image} alt="Game" />}
      {header && <h1 className="text-2xl font-bold">{header}</h1>}
      {content && <p className="text-white-700 text-base">{content}</p>}
    </div>
  );
};

Card.propTypes = {
  children: propTypes.node,
  image: propTypes.string,
  header: propTypes.string,
  content: propTypes.string,
};

export default Card;
