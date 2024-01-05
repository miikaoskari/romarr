import React from 'react';
import propTypes from 'prop-types';
const Grid = ({children}) => {
    return (
        <div className={"grid grid-cols-4 mx-4 my-2"}>
            {children}
        </div>
    );
};

Grid.propTypes = {
    children: propTypes.node,
}

export default Grid;