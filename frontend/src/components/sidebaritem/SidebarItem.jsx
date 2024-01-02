import React from 'react';

const SidebarItem = ({children}) => {
    return (
        <div className="m-2 bg-white rounded-2xl flex-grow">
            {children}
        </div>
    );
};

export default SidebarItem;