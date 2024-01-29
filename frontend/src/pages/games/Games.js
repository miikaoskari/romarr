import Grid from '../../components/grid/Grid';
import React, { useEffect } from 'react';
import { Card } from '../../components';
const Games = () => {
  const [data, setData] = React.useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/api/v1/games')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => setData(data))
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  return (
    <div className='bg-gray-900 rounded-3xl '>
      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Games</h1>
      </div>
      {data.length > 0 ? (
        <Grid>
          {data.map((image) => (
            <Card key={image.id} image={image} />
          ))}
        </Grid>
      ) : (
        <div className={"flex justify-center items-center h-full"}>
          <p className={"text-gray-700"}>No games available</p>
        </div>
      )
      }

    </div>
  );
};

export default Games;
