import React from 'react';
import { Card, Grid } from '../../components';

const Settings = () => {
  const [indexers, setIndexers] = React.useState([]);
  const [clients, setClients] = React.useState([]);

  React.useEffect(() => {
    fetch('http://localhost:3000/api/v1/indexers')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((indexers) => setIndexers(indexers))
      .catch((error) => {
        console.error('Error:', error);
      });
  });

  React.useEffect(() => {
    fetch('http://localhost:3000/api/v1/clients')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((clients) => setClients(clients))
      .catch((error) => {
        console.error('Error:', error);
      });
  });

  return (
    <div>
      <div className="flex flex-col py-3">
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Indexers</h1>
      </div>
      <div className={''}>
        {indexers.length > 0 ? (
          <Grid>
            {indexers.map((indexer) => (
              <Card key={indexer.id} indexer={indexer} />
            ))}
          </Grid>
        ) : (
          <div className={'flex h-full items-center justify-center'}>
            <p className={'my-4 text-gray-700'}>No indexers configured</p>
          </div>
        )}
      </div>
      <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Download clients</h1>
      <div className={''}>
        {clients.length > 0 ? (
          <Grid>
            {clients.map((client) => (
              <Card key={client.id} client={client} />
            ))}
          </Grid>
        ) : (
          <div className={'flex h-full items-center justify-center'}>
            <p className={'my-4 text-gray-700'}>No indexers configured</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Settings;
