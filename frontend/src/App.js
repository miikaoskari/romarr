import React from 'react';
import './App.css';
import {Article, Brand, Cta, Feature, Navbar, Sidebar} from "./components";
import {Footer, Header, Features, Blog} from "./containers";
import {About, Activity, Dashboard, Games, Settings} from "./pages";
import {Routes, Route} from 'react-router-dom';

function App() {
    return (
        <div className="App">
            <div className="container__navbar">
                <Navbar></Navbar>
            </div>
            <Routes>
                <Route path="/" element={<Dashboard/>}/>
                <Route path={"/about"} element={<About/>}/>
                <Route path={"/activity"} element={<Activity/>}/>
                <Route path={"/games"} element={<Games/>}/>
                <Route path={"/settings"} element={<Settings/>}/>
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
