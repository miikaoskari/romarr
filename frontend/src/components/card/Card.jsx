import React from 'react';
import propTypes from 'prop-types';

const Card = ({
  children,
  name = "N/A",
  cover = "N/A",
  platforms = [],
  rating = "N/A",
}) => {
  return (
    <div className="max-h-md auto mx-2 my-2 max-w-md rounded-3xl border-2 border-gray-800 bg-gray-800 p-6 shadow-md">
      {children}
      {name && <p className="text-white-700 text-base">{name}</p>}
      {cover && <p className="text-white-700 text-base">{cover}</p>}
      {platforms && <p className="text-white-700 text-base">{platforms}</p>}
      {rating && <p className="text-white-700 text-base">{rating}</p>}
    </div>
  );
};

Card.propTypes = {
  children: propTypes.node,
  name: propTypes.string,
  cover: propTypes.string,
  platforms: propTypes.array,
  rating: propTypes.string,
};

export default Card;
