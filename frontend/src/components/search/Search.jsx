import React from 'react';

const Search = (props) => {
    const { name, summary, release_dates, cover_url } = props.data;
    console.log(props.data);
    return (

        <div>
            <img className={""} src={cover_url} alt={name}/>
            <h1 className={"text-2xl"}>{name}</h1>
            <p>{summary}</p>
        </div>
    );
};

export default Search;