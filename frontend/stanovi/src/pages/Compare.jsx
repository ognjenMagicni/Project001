import React from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';
import '../css/Compare.css'
import { useState, useEffect } from 'react';


const Compare = () => {
    const [firstOption, setFirstOption] = useState('Option 1');
    const [secondOption, setSecondOption] = useState('Option A');
    const [currentImageIndex, setCurrentImageIndex] = useState(0);
  
    const [firstDropdownOptions, setFirstDropdownOptions] = useState([])
    const [secondDropdownOptions, setSecondDropdownOptions] = useState([])
    const images = [
      'distributionOfSquarePriceBasedOnSquareMetresCompare.png',
      'distributionOfSquarePricesCompare.png',
      'fullAndSquarePriceCompare.png',
    ];
  
    

    useEffect(  () => {
        async function currFunction(){
            const res = await axios.get('http://localhost:8000/getAllSearches/')

            const transformedData = res.data.map((item) => ({
                id:item[0],
                title:item[1]
            }));

            setFirstDropdownOptions(transformedData)
            setSecondDropdownOptions(transformedData)

            console.log(firstDropdownOptions)

            setFirstOption(transformedData[0].id)
            setSecondOption(transformedData[0].id)
        }
        currFunction()
    },[])

    const handleLeftClick = () => {
      setCurrentImageIndex((prevIndex) => (prevIndex === 0 ? images.length - 1 : prevIndex - 1));
    }
  
    const handleRightClick = () => {
      setCurrentImageIndex((prevIndex) => (prevIndex === images.length - 1 ? 0 : prevIndex + 1));
    };

    const handleClick = async () => {
        await axios.get(`http://localhost:8000/getAnalyticsCompare/${firstOption}/${secondOption}`)
    }
  
    return (
      <div className="container">
        {/* First Row: Two Dropdowns */}
        <div className="dropdown-row">
          <div className="dropdown-group">
            <label htmlFor="firstOptions" className="dropdown-label">First Option:</label>
            <select
              id="firstOptions"
              className="dropdown"
              value={firstOption}
              onChange={(e) => setFirstOption(e.target.value)}
            >
              {firstDropdownOptions.map((item) => (
                <option key={item.id} value={item.id}>{item.title}</option>
              ))}
            </select>
          </div>
          <div className="dropdown-group">
            <label htmlFor="secondOptions" className="dropdown-label">Second Option:</label>
            <select
              id="secondOptions"
              className="dropdown"
              value={secondOption}
              onChange={(e) => setSecondOption(e.target.value)}
            >
              {secondDropdownOptions.map((item) => (
                <option key={item.id} value={item.id}>{item.title}</option>
              ))}
            </select>
          </div>
        </div>
  
        {/* Second Row: Button */}
        <div className="button-row">
          <button
            className="compare-button"
            onClick={handleClick}
          >
            Compare
          </button>
        </div>
  
        {/* Third Row: Image Carousel */}
        <div className="carousel-row">
          <button className="carousel-button" onClick={handleLeftClick}>Left</button>
          <img
            src={images[currentImageIndex]}
            alt={`Image ${currentImageIndex + 1}`}
            className="carousel-image"
          />
          <button className="carousel-button" onClick={handleRightClick}>Right</button>
        </div>
      </div>
    );
  };
  
  export default Compare;