import React from 'react';
import { Card, Grid } from '../../components';

const Settings = () => {
  return (
    <div>
      <div className="flex flex-col py-3">
        <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Indexers</h1>
      </div>
      <div className={''}>
        <Grid>
          <Card>Newznab</Card>
          <Card>Torznab</Card>
        </Grid>
      </div>
      <h1 className={'mx-6 place-items-start text-3xl font-bold'}>Download clients</h1>
      <div className={''}>
        <Grid>
          <Card>SABnzbd</Card>
          <Card>qBittorrent</Card>
        </Grid>
      </div>
    </div>
  );
};

export default Settings;
