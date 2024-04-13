import React from 'react';
import propTypes from 'prop-types';
import { faFrown, faMeh, faSmile } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const SmileyRating = ({ rating, size }) => {
  let smiley = faMeh;
  let color = 'yellow';

  if (rating > 66) {
    smiley = faSmile;
    color = 'lightgreen';
  } else if (rating > 33) {
    smiley = faMeh;
    color = 'yellow';
  } else {
    smiley = faFrown;
    color = 'red';
  }

  return <FontAwesomeIcon icon={smiley} size={size} color={color} />;
};

SmileyRating.propTypes = {
  rating: propTypes.number.isRequired,
  size: propTypes.string.isRequired,
};

export default SmileyRating;
