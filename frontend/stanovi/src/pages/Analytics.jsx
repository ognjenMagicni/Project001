import React from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';
import { useState, useEffect } from 'react';
import '../css/Analytics.css'

/*class Analytics extends React.Component {
    constructor(props) {
        super(props);
        const path = 'C:/Users/Asus/Desktop/Slike'
        this.state = {
            currentImageIndex: 0,
            images: [
                "/histogramOfLocations.png",
                "/distributionOfSquarePrices.png",
                "/distributionByLocation.png",
                "/fullAndSquarePrice.png",
                "/distributionOfSquarePriceBasedOnSquareMetres.png"
            ]
        };
    }

    componentDidMount = () => {
        console.log("Fetching analytics");
        //this.getAnalytics();
        
    }

    getAnalytics = async () => {
        let pathVariable = this.getPathVariable();
        await axios.get(`http://localhost:8000/getAnalytics/${pathVariable}`)
    }

    getPathVariable = () => {
        let path = window.location.pathname;
        let pathArray = path.split('/');
        return pathArray[pathArray.length - 1];
    }

    handleClick = () => {
        this.getAnalytics();
    }

    handleNext = () => {
        this.setState(prevState => ({
            currentImageIndex: (prevState.currentImageIndex + 1) % prevState.images.length
        }));
    };

    handlePrev = () => {
        this.setState(prevState => ({
            currentImageIndex: (prevState.currentImageIndex - 1 + prevState.images.length) % prevState.images.length
        }));
    };

    render() {
        const { currentImageIndex, images } = this.state;
        return (
            <div className="analytics-container">
                <div className="analytics-column">
                    <button onClick={this.handleClick}>Bitno dugme</button>
                    <h1 className="analytics-title">Main Title</h1>
                    <p className="analytics-description">This is a detailed description of the analytics content.</p>
                </div>
                <div className="analytics-column">
                    <h3 className="analytics-subtitle">Related Images</h3>
                    <div className="analytics-image-viewer">
                        <button className="analytics-arrow" onClick={this.handlePrev}>◀</button>
                        
                        <img 
                            src={images[currentImageIndex]} 
                            alt="Analytics" 
                            className="analytics-image"
                        />
                        <button className="analytics-arrow" onClick={this.handleNext}>▶</button>
                    </div>
                </div>
            </div>
        );
    }
}

export default Analytics;*/


function Analytics() {

    const [currentImageIndex, setCurrentImageIndex] = useState(0);
    const [images, setImages] = useState(["/histogramOfLocations.png",
                "/distributionOfSquarePrices.png",
                "/distributionByLocation.png",
                "/fullAndSquarePrice.png",
                "/distributionOfSquarePriceBasedOnSquareMetres.png"]);
    const [searchInfo,setSearchInfo] = useState("Title")
    const [descriptionInfo,setDescriptionInfo] = useState("Description")

    function getPathVariable(){
        let path = window.location.pathname;
        let pathArray = path.split('/');
        return pathArray[pathArray.length - 1];
    }
    
    useEffect(() =>{
        async function getInfo(){
            const id_search = getPathVariable()
            const result = await axios.get(`http://localhost:8000/getSearch/${id_search}`)
            setSearchInfo(result.data[0][1])
            setDescriptionInfo(result.data[0][2])
        }
        getInfo()
    },[searchInfo,descriptionInfo])
    
    function handlePrev(){
        setCurrentImageIndex((currentImageIndex-1)%5)
    }

    function getPathVariable(){
        let path = window.location.pathname;
        let pathArray = path.split('/');
        return pathArray[pathArray.length - 1];
    }

    function handleNext(){
        setCurrentImageIndex((currentImageIndex+1)%5)
    }

    const DeleteWithConfirmation = () => {
        const [showConfirmation, setShowConfirmation] = useState(false);
      
        const handleDelete = () => {
            console.log("Item deleted!"); // Replace with your delete logic
            setShowConfirmation(false); // Close the confirmation dialog
        };
    }

    return (
        <div className="analytics-container">
            <div className="analytics-column-info">
                <h1 className="analytics-title">{searchInfo}</h1>
                <p className="analytics-description">{descriptionInfo}</p>
            </div>
            <div className="analytics-column-picture">
                <h3 className="analytics-subtitle">Related Images</h3>
                <div className="analytics-image-viewer">
                    <button className="analytics-arrow" onClick={handlePrev}>◀</button>
                    
                    <img 
                        src={images[currentImageIndex]} 
                        alt="Analytics" 
                        className="analytics-image"
                    />
                    <button className="analytics-arrow" onClick={handleNext}>▶</button>
                </div>
            </div>
        </div>
    )
    
}

export default Analytics