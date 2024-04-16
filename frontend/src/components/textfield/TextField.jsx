import React from 'react';

const TextField = () => {
  return (
    <div>
      <input
        type={'text'}
        className={
          'focus:shadow-outline" id="username w-full appearance-none rounded border px-3 py-2 leading-tight text-gray-700 shadow focus:outline-none'
        }
      ></input>
    </div>
  );
};

export default TextField;
