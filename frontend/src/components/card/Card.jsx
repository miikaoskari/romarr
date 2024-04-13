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
      {cover && <p className="text-white-700 text-base mt-2">{cover}</p>}
      {name && <p className="text-white-700 text-base font-bold">{name}</p>}
      {platforms && <p className="text-white-700 text-base mt-2">{platforms}</p>}
      {rating && <p className="text-white-700 text-base">{rating.toFixed(1)}</p>}
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
