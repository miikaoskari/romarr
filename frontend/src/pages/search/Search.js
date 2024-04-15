import React, { useEffect } from 'react';
import { SearchCard, Grid } from '../../components';

const Search = () => {
  const [results, setResults] = React.useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/api/v1/games')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => setResults(data))
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);
  return (
    <div>
      <Grid>
        {results.map((game) => (
            <SearchCard
              key={game.id}
              name={game.name}
              cover_url={game.cover_path}
              platforms={game.platforms.map(platform => platform.platform)}
              rating={game.rating}
              release_dates={game.release_dates.map(date => date.release_date)}
            />
          ))}

      </Grid>
    </div>
  );
};

export default Search;
