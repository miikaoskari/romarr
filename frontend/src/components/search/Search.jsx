import React from "react";

const Search = () => {
  return (
    <div className={"order-last flex justify-end"}>
      <input
        className={"mx-6 my-2 rounded-2xl border-2 bg-gray-200 py-1 indent-2"}
        placeholder={"Search"}></input>
    </div>
  );
};

export default Search;
