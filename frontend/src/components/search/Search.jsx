import React from 'react';

const Search = () => {
    return (
        <div className={"flex justify-end order-last"}>
            <input className={"my-2 mx-6 border-2 rounded-2xl bg-gray-200 py-1 indent-2"}
                   placeholder={"Search"}></input>
        </div>
    );
};

export default Search;