import React from 'react';
import './App.css';
import { Article, Brand, Cta, Feature, Navbar, Sidebar} from "./components";
import { Footer, Header, Features, Blog} from "./containers";

function App() {
  return (
    <div className="App">
      <div className="solid__bg">
          <Navbar></Navbar>
          <Header></Header>
      </div>
        <Brand></Brand>
        <Features></Features>
        <Cta></Cta>
        <Blog></Blog>
        <Footer></Footer>
    </div>
  );
}

export default App;
