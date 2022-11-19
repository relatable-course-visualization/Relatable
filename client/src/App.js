import './App.css';
import NewSearch from './components/newSearch';
import Homepage from "./home/homepage"
import {Helmet} from "react-helmet";



function App() {
  return (
    <>
      <Helmet>
        <title>Relatable</title>
      </Helmet>
      <Homepage />
    </>
  )
     
}

export default App;
