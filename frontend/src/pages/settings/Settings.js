import React, { useState } from 'react';
import { Button, Card, Grid, Modal } from '../../components';

const Settings = () => {
  const [isOpen, setIsOpen] = useState({ type: '', open: false });

  function closeModal() {
    setIsOpen({ type: '', open: false });
  }

  function openModal(type) {
    setIsOpen({ type: type, open: true });
  }

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
    <div className="rounded-3xl bg-gray-900 ">
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
      <div className={'px-6 py-4'}>
        <Button title={'Add'} onClick={() => openModal('indexer')}></Button>
      </div>
      {isOpen.type === 'indexer' && <Modal isOpen={isOpen.open} closeModal={closeModal} title={'Add indexer'}></Modal>}
      <div className="flex flex-col py-3">
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Download clients</h1>
      </div>
      <div className={''}>
        {clients.length > 0 ? (
          <Grid>
            {clients.map((client) => (
              <Card key={client.id} client={client} />
            ))}
          </Grid>
        ) : (
          <div className={'flex h-full items-center justify-center'}>
            <p className={'my-4 text-gray-700'}>No download clients configured</p>
          </div>
        )}
      </div>
      <div className={'px-6 py-4'}>
        <Button title={'Add'} onClick={() => openModal('client')}></Button>
      </div>
      {isOpen.type === 'client' && (
        <Modal isOpen={isOpen.open} closeModal={closeModal} title={'Add download client'}></Modal>
      )}
    </div>
  );
};

export default Settings;
