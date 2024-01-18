import React from 'react';
import propTypes from 'prop-types';

const Button = ({ title, onClick }) => {
  return (
    <div>
      <button
        onClick={onClick}
        type={'button'}
        className={
          'inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2'
        }
      >
        {title}
      </button>
    </div>
  );
};

Button.propTypes = {
  title: propTypes.string.isRequired,
  onClick: propTypes.func.isRequired,
};

export default Button;
