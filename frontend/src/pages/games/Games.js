import Grid from '../../components/grid/Grid';
import React, { useEffect } from 'react';
import { Card } from '../../components';

const Games = () => {
  const [data, setData] = React.useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/games/all')
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
    <div className="rounded-3xl bg-gray-900 ">
      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Games</h1>
      </div>
      {data.length > 0 ? (
        <Grid>
          {data.map((game) => (
            <Card
              key={game.id}
              name={game.name}
              cover={game.cover}
              platforms={game.platforms.map(platform => platform.platform)}
              rating={game.rating}
              release_dates={game.release_dates.map(date => date.release_date)}
            />
          ))}
        </Grid>
      ) : (
        <div className={'flex h-full items-center justify-center'}>
          <p className={'text-gray-700'}>No games available</p>
        </div>
      )}
    </div>
  );
};

export default Games;
