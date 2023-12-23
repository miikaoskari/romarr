import Grid from '../../components/grid/Grid';
import React from "react";
const Games = () => {
    return (
        <div>
            <div className={"flex flex-col py-3"}>
                <h1 className={"text-3xl font-bold place-items-start mx-40"}>Games</h1>
            </div>
            <Grid></Grid>
        </div>
    );
};

export default Games;