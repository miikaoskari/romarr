import React from 'react';
import PropTypes from 'prop-types';

const RoundedBox = ({children}) => {
    return (
        <div className="m-2 bg-white rounded-2xl flex-grow">
            {children}
        </div>
    );
};

RoundedBox.propTypes = {
    children: PropTypes.node,
}

export default RoundedBox;