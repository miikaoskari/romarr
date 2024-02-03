import React, { useEffect } from 'react';
import { Card, Grid } from '../../components';

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
        {results.map((image) => (
          <Card key={image.id} image={image} />
        ))}
      </Grid>
    </div>
  );
};

export default Search;
