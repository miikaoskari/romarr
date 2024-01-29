import { Table } from '../../components';
import React, { useEffect, useState } from 'react';

const Activity = () => {
  const [data, setData] = useState([]);

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
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Queue</h1>
      </div>
      {data.length > 0 ? (
        <div className={'mx-6'}>
          <Table></Table>
        </div>
      ) : (
        <div className={'flex h-full items-center justify-center'}>
          <p className={'text-white-700'}>Queue is empty</p>
        </div>
      )}

      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>History</h1>
      </div>
      {data.length > 0 ? (
        <div className={'mx-6'}>
          <Table></Table>
        </div>
      ) : (
        <div className={'flex h-full items-center justify-center'}>
          <p className={'text-white-700'}>History is empty</p>
        </div>
      )}

      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Blocklist</h1>
      </div>
      {data.length > 0 ? (
        <div className={'mx-6'}>
          <Table></Table>
        </div>
      ) : (
        <div className={'flex h-full items-center justify-center'}>
          <p className={'text-white-700'}>Blocklist is empty</p>
        </div>
      )}

    </div>
  );
};

export default Activity;
