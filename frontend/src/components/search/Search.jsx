import React from 'react';

const Search = () => {

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      history.push('/search');
    }
  };

  return (
<div className="order-last flex justify-end">
    <input
        className="mx-2 my-2 rounded-2xl bg-gray-800 py-1 px-4 w-24  indent-2 outline-none hover:shadow-lg transition-all text-white focus:w-60"
        placeholder="Search"
        onKeyDown={handleKeyPress}
    ></input>
</div>

  );
};

export default Search;
