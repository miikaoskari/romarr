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
        className="mx-2 my-2 w-24 rounded-2xl bg-gray-800 px-4 py-1  indent-2 text-white outline-none transition-all hover:shadow-lg focus:w-60"
        placeholder="Search"
        onKeyDown={handleKeyPress}
      ></input>
    </div>
  );
};

export default Search;
