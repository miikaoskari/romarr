import React from 'react';
import propTypes from 'prop-types';
const Grid = ({ children }) => {
  return <div className={'mx-4 my-2 grid grid-cols-4 p-3'}>{children}</div>;
};

Grid.propTypes = {
  children: propTypes.node,
};

export default Grid;
