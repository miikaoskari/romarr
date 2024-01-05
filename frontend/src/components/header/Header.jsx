import React from 'react';

const Header = ({children}) => {
    return (
        <div className={"flex items-center"}>
            {React.Children.map(children, child => (
                <div className={"flex-1"}>
                    {child}
                </div>
            ))}
        </div>
    );
};

export default Header;