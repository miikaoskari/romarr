import Grid from '../../components/grid/Grid';
import React, { useEffect } from 'react';
import { Card } from '../../components';
const Games = () => {
  const [image, setImage] = React.useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/api/v1/games')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => setImage(data))
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  return (
    <div>
      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Games</h1>
      </div>

      <Grid>
        {image.map((image) => (
          <Card key={image.id} image={image} />
        ))}
      </Grid>
    </div>
  );
};

export default Games;
