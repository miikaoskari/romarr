import React, { useState } from 'react';
import { Button } from '../index';

const Search = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [data, setData] = useState([]);

  const handleChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(searchTerm);
    fetch(`http://localhost:8080/api/search/${searchTerm}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        window.location.href = `/search/${searchTerm}`;
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit} className={'flex items-center justify-center'}>
      <input
        className="mx-2 my-2 h-10 w-60 rounded-2xl bg-gray-800 px-4 py-1 indent-2 text-white outline-none transition-all hover:shadow-lg"
        type="text"
        placeholder="Search..."
        value={searchTerm}
        onChange={handleChange}
      ></input>
      <Button onClick={handleSubmit} title={'Search'}></Button>
    </form>
  );
};

export default Search;
