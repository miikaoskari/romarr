import React from 'react';
import propTypes from 'prop-types';
const SidebarItem = ({children}) => {
    return (
        <div className="m-2 bg-white rounded-2xl flex-grow">
            {children}
        </div>
    );
};

SidebarItem.propTypes = {
    children: propTypes.node,
}

export default SidebarItem;