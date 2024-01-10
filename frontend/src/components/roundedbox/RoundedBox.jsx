import React from 'react';
import PropTypes from 'prop-types';

const RoundedBox = ({ children }) => {
  return <div className="m-2 flex-grow rounded-2xl bg-white">{children}</div>;
};

RoundedBox.propTypes = {
  children: PropTypes.node,
};

export default RoundedBox;
