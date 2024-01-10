import React from 'react';
import propTypes from 'prop-types';
const SidebarItem = ({ children }) => {
  return <div className="m-2 flex-grow rounded-2xl bg-white">{children}</div>;
};

SidebarItem.propTypes = {
  children: propTypes.node,
};

export default SidebarItem;
