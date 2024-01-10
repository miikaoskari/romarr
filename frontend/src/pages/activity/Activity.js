import { Table } from '../../components';
import React from 'react';

const Activity = () => {
  return (
    <div>
      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-40 place-items-start text-3xl font-bold'}>Queue</h1>
      </div>
      <Table></Table>
      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-40 place-items-start text-3xl font-bold'}>History</h1>
      </div>
      <Table></Table>
      <div className={'flex flex-col py-3'}>
        <h1 className={'mx-40 place-items-start text-3xl font-bold'}>Blocklist</h1>
      </div>
      <Table></Table>
    </div>
  );
};

export default Activity;
