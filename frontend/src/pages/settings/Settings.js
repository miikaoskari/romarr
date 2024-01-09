import React from "react";
import { Card, Grid } from '../../components';

const Settings = () => {
    return (
        <div>
            <div className="flex flex-col py-3">
            <h1 className={"text-3xl font-bold place-items-start mx-6"}>Indexers</h1>
            </div>
            <div className={""}>
              <Grid>
                <Card>Newznab</Card>
                <Card>Torznab</Card>
              </Grid>
            </div>
            <h1 className={"text-3xl font-bold place-items-start mx-6"}>Download clients</h1>
            <div className={""}>
              <Grid>
                <Card>SABnzbd</Card>
                <Card>qBittorrent</Card>
              </Grid>
            </div>
        </div>
    )
        ;
};

export default Settings;