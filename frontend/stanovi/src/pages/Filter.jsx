// Import React and useState
import React, { useEffect, useState } from "react";
import "../css/Filter.css"; // External CSS for styling
import axios from 'axios'
import { Link } from 'react-router-dom';


const Filter = () => {
  // State to handle form inputs
  const [formData, setFormData] = useState({
    id_search: "",
    minPrice: "",
    maxPrice: "",
    minSquareMetres: "",
    maxSquareMetres: "",
    minSquarePrices: "",
    maxSquarePrices: ""
  });
  const [infoData,setInfoData] = useState({
    minPrice: "",
    maxPrice: "",
    minSquareMeters: "",
    maxSquareMeters: ""
  })
  const [idSearch,setIdSearch] = useState()


    function getPathVariable(){
    	let path = window.location.pathname;
    	let pathArray = path.split('/');
    	return pathArray[pathArray.length - 1];
	}

  useEffect( ()=>{
	async function currFunction(){
		const id_search1 = getPathVariable()
		setIdSearch(id_search1)
		const search = await axios.get(`http://localhost:8000/getSearch/${id_search1}`)
		const solution = {
      minPrice: search.data[0][3],
			maxPrice: search.data[0][4],
			minSquareMeters: search.data[0][5],
			maxSquareMeters: search.data[0][6],
		}
		setInfoData(solution)
    setFormData((formData) => ({
      ...formData, // Spread the existing fields
      ['id_search']: id_search1, // Update only the specified field
    }));
	}
	currFunction()
  },[] )

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault()
    async function currFunction(){
      console.log(formData)
      await axios.post('http://localhost:8000/runGraph',formData)
    }
    currFunction()
  };

  return (
    <form className="filter-form" >
      <div className="form-group">
        <label>Min Price:</label>
        <input
          type="number"
          name="minPrice"
          value={formData.minPrice}
          onChange={handleChange}
          placeholder="Enter min price"
        />
      </div>
      <div className="form-group">
        <label>Max Price:</label>
        <input
          type="number"
          name="maxPrice"
          value={formData.maxPrice}
          onChange={handleChange}
          placeholder="Enter max price"
        />
      </div>
      <div className="form-group">
        <label>Min Square Meters:</label>
        <input
          type="number"
          name="minSquareMetres"
          value={formData.minSquareMetres}
          onChange={handleChange}
          placeholder="Enter min square meters"
        />
      </div>
      <div className="form-group">
        <label>Max Square Meters:</label>
        <input
          type="number"
          name="maxSquareMetres"
          value={formData.maxSquareMetres}
          onChange={handleChange}
          placeholder="Enter max square meters"
        />
      </div>
      <div className="form-group">
        <label>Min Square Price:</label>
        <input
          type="number"
          name="minSquarePrices"
          value={formData.minSquarePrices}
          onChange={handleChange}
          placeholder="Enter min square price"
        />
      </div>
      <div className="form-group">
        <label>Max Square Price:</label>
        <input
          type="number"
          name="maxSquarePrices"
          value={formData.maxSquarePrices}
          onChange={handleChange}
          placeholder="Enter max square price"
        />
      </div>
      <div className="summary">
        <h3>Filter Summary</h3>
        <p>Min Price: {infoData.minPrice || "Not set"}</p>
        <p>Max Price: {infoData.maxPrice || "Not set"}</p>
        <p>Min Square Meters: {infoData.minSquareMeters || "Not set"}</p>
        <p>Max Square Meters: {infoData.maxSquareMeters || "Not set"}</p>
      </div>
      <button onClick={handleSubmit} className="submit-button">Apply Filters</button>
    </form>
  );
};

export default Filter;