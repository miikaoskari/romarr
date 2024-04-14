import React from 'react';
import propTypes from 'prop-types';
import { SmileyRating } from '../index';

const Card = ({
  children,
  name = "N/A",
  cover_url = "N/A",
  platforms = [],
  rating = "N/A",
}) => {
  const baseUrl = "http://localhost:8000";

  return (
    <div className="max-h-md auto mx-2 my-2 max-w-md rounded-3xl border-2 border-gray-800 bg-gray-800 p-6 shadow-md">
      {children}
      {cover_url && <img src={`${baseUrl}/${cover_url}`} alt={name} className="w-full h-64 rounded-md"/>}
      {name && <p className="text-white-700 text-base font-bold">{name}</p>}
      {platforms && <p className="text-white-700 text-base mt-2">{platforms}</p>}
      {rating && <SmileyRating rating={rating | 0} size={"lg"}/>}
    </div>
  );
};

Card.propTypes = {
  children: propTypes.node,
  name: propTypes.string,
  cover_url: propTypes.string,
  platforms: propTypes.array,
  rating: propTypes.number,
};

export default Card;
