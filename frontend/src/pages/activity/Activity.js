import {Table} from "../../components";
import React from "react";


const Activity = () => {
    return (
        <div>
            <div className={"flex flex-col py-3"}>
                <h1 className={"text-3xl font-bold place-items-start mx-40"}>Queue</h1>
            </div>
            <Table></Table>
            <div className={"flex flex-col py-3"}>
                <h1 className={"text-3xl font-bold place-items-start mx-40"}>History</h1>
            </div>
            <Table></Table>
            <div className={"flex flex-col py-3"}>
                <h1 className={"text-3xl font-bold place-items-start mx-40"}>Blocklist</h1>
            </div>
            <Table></Table>
        </div>
    )
        ;
};

export default Activity;
