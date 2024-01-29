import React, { Fragment, useState } from 'react';
import { Button, Card, Grid } from '../../components';
import { Dialog, Transition } from '@headlessui/react';

const Settings = () => {
  let [isOpen, setIsOpen] = useState(false);

  function closeModal() {
    setIsOpen(false);
  }

  function openModal() {
    setIsOpen(true);
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
    <div className='bg-gray-900 rounded-3xl '>
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
            <p className={'my-4 text-gray-200'}>No indexers configured</p>
          </div>
        )}
      </div>
      <div className={'px-6 py-4'}>
        <Button title={'Add'} onClick={openModal}></Button>
      </div>
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
            <p className={'my-4 text-gray-200'}>No indexers configured</p>
          </div>
        )}
      </div>
      <div className={'px-6 py-4'}>
        <Button title={'Add'} onClick={openModal}></Button>
      </div>
      <Transition appear show={isOpen} as={Fragment}>
        <Dialog as="div" className="relative z-10" onClose={closeModal}>
          <Transition.Child
            as={Fragment}
            enter="ease-out duration-300"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in duration-200"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
          >
            <div className="fixed inset-0 bg-black/25" />
          </Transition.Child>

          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <Transition.Child
                as={Fragment}
                enter="ease-out duration-300"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-200"
                leaveFrom="opacity-100 scale-100"
                leaveTo="opacity-0 scale-95"
              >
                <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                  <Dialog.Title as="h3" className="text-lg font-medium leading-6 text-gray-900">
                    Add Indexer
                  </Dialog.Title>
                  <div className="mt-2">
                    <p className="text-sm text-gray-500">

                    </p>
                  </div>

                  <div className="mt-4">
                    <Button title={"Save"} onClick={closeModal}></Button>
                  </div>
                </Dialog.Panel>
              </Transition.Child>
            </div>
          </div>
        </Dialog>
      </Transition>
    </div>
  );
};

export default Settings;
