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
    <div>
      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Queue</h1>
      </div>
      {data.length > 0 ? (
        <Table></Table>
      ) : (
        <div className={'flex justify-center items-center h-full'}>
          <p className={'text-gray-700'}>Queue is empty</p>
        </div>
      )
      }

      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>History</h1>
      </div>
      <Table></Table>
      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Blocklist</h1>
      </div>
      <Table></Table>
    </div>
  );
};

export default Activity;
