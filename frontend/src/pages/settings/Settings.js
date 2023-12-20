import {Indexers} from "../../components";
import React from "react";

const Settings = () => {
    return (
        <div>
            <div className="flex flex-col py-3">
            <h1 className={"text-3xl font-bold place-items-start mx-40"}>Indexers</h1>
            </div>
            <div className={""}>
                <Indexers></Indexers>
            </div>
        </div>
    )
        ;
};

export default Settings;