import React from 'react';
import propTypes from 'prop-types';

const Card = ({ children, image, header, content }) => {
  return (
    <div className="max-h-md auto mx-2 my-2 max-w-md rounded-lg border-2 border-gray-50 bg-white p-6 shadow-md">
      {children}
      {image && <img src={image} alt="Game"/>}
      {header && <h1 className="text-2xl font-bold">{header}</h1>}
      {content && <p className="text-gray-700 text-base">{content}</p>}
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
