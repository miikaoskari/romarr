import React from 'react';

const Card = ({children}) => {
    return (
        <div className="rounded-lg shadow-md p-6 bg-white mx-2 my-2 max-w-md max-h-md auto">
            {children}
        </div>
    );
};

export default Card;