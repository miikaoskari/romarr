import React from 'react';

const Grid = ({children}) => {
    return (
        <div className={"grid grid-cols-4 mx-4 my-2"}>
            {children}
        </div>
    );
};

export default Grid;