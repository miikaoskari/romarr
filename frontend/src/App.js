import React from 'react';
import './App.css';
import {Layout, Navbar, Sidebar} from "./components";
import {Footer, Header} from "./containers";
import {About, Activity, Dashboard, Games, Settings, Login} from "./pages";
import {Routes, Route} from 'react-router-dom';

function App() {
    return (
        <div className="App bg-gray-800">
            <Layout></Layout>
        </div>
    );
}

export default App;
