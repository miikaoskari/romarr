import React from 'react';

const Search = () => {

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      history.push('/search');
    }
  };

  return (
    <div className={'order-last flex justify-end'}>
      <input className={'mx-2 my-2 rounded-2xl border-2 bg-gray-200 py-1 indent-2'} placeholder={'Search'} onKeyDown={handleKeyPress}></input>
    </div>
  );
};

export default Search;
