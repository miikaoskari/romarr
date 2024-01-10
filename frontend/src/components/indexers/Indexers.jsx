import React from 'react';
import propTypes from 'prop-types';
const Indexers = ({ children }) => {
  return <div>{children}</div>;
};

Indexers.propTypes = {
  children: propTypes.node,
};

export default Indexers;
