import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter,Routes,Route} from "react-router-dom"
import Interface from "./pages/Interface.jsx"
import Graph from "./pages/Graph.jsx"
import Menu from "./pages/Menu.jsx"
import Analytics from './pages/Analytics.jsx';
import Compare from './pages/Compare.jsx';  
import Search from './pages/Search.jsx';
import List from './pages/List.jsx';
import Properties from './pages/Properties.jsx';
import Filter from './pages/Filter.jsx'


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <div>
    <BrowserRouter>
      <Routes>
        <Route path="/homepage" element={<Interface/>}></Route>
        <Route path="/graph/:id" element={<Graph/>}></Route>
        <Route path="/menu" element={<Menu/>}></Route>
        <Route path="/analytics/:id_search" element={<Analytics/>}></Route>
        <Route path="/compare" element={<Compare/>}></Route>
        <Route path="/search" element={<Search/>}></Route>
        <Route path="/list" element={<List/>}></Route>
        <Route path="/properties" element={<Properties/>}></Route>
        <Route path="/filter/:id" element={<Filter/>}></Route>
      </Routes>
    </BrowserRouter>
  </div>
);

reportWebVitals();
