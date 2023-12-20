import React from 'react';
import './App.css';
import {Article, Brand, Cta, Feature, Navbar, Sidebar} from "./components";
import {Footer, Header, Features, Blog} from "./containers";
import {About, Activity, Dashboard, Games, Settings, Login} from "./pages";
import {Routes, Route, useLocation} from 'react-router-dom';

function App() {
    const location = useLocation();
    return (
        <div className="App">
            {location.pathname !== '/login' && (
                <div className="container__navbar">
                    <Navbar></Navbar>
                </div>
            )}
            <Routes>
                <Route path="/" element={<Dashboard/>}/>
                <Route path={"/about"} element={<About/>}/>
                <Route path={"/activity"} element={<Activity/>}/>
                <Route path={"/games"} element={<Games/>}/>
                <Route path={"/settings"} element={<Settings/>}/>
                <Route path={"/login"} element={<Login/>}/>
            </Routes>

            <div className="container__body">
                <Header></Header>
                <Footer></Footer>
            </div>
        </div>
    )
        ;
}

export default App;
