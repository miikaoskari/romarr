import React from 'react';
import {RoundedBox, Sidebar} from "../index";
import {About, Activity, Dashboard, Games, Settings, Login} from "../../pages";
import {useLocation} from "react-router-dom";

const Layout = () => {
    const location = useLocation();
    let MainContent;

    switch(location.pathname) {
        case '/':
            MainContent = <Dashboard/>;
            break;
        case '/about':
            MainContent = <About/>;
            break;
        case '/activity':
            MainContent = <Activity/>;
            break;
        case '/games':
            MainContent = <Games/>;
            break;
        case '/settings':
            MainContent = <Settings/>;
            break;
        case '/login':
            MainContent = <Login/>;
            break;
        default:
            MainContent = <Dashboard/>;
    }

    return (
        <div className="flex">
            <Sidebar/>
            <RoundedBox>
                {MainContent}
            </RoundedBox>
        </div>
    );
};

export default Layout;