import logo from './logo.svg';
import './App.css';
import { Article, Brand, Cta, Feature, Navbar} from "./components";
import { Footer, Header, Features, Blog} from "./containers";


function App() {
  return (
    <div className="App">
      <div className="gradient__bg">
          <Navbar></Navbar>
          <Header></Header>
      </div>
    </div>
  );
}

export default App;
