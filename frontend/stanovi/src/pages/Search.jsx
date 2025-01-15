import React from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';
import '../css/Search.css'

class Search extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pages: '',
            location: '',
            type: '',
            minPrice: '',
            maxPrice: '',
            title: '',
            description: '',
            typeList:[],
            locationList:[]
        };
    }

    componentDidMount = () => {
        this.getTypeList()
        this.getLocationList()
    }

    getTypeList = async () => {
        let types = await axios.get("http://localhost:8000/getTypes/")
        this.setState({typeList:types.data})
    }

    getLocationList = async () => {
        let locations = await axios.get("http://localhost:8000/getLocations/")
        this.setState({locationList:locations.data})
    }

    handleChange = (e) => {
        const { name, value } = e.target;
        this.setState({ [name]: value });
    };

    handleSubmit = async (e) => {
        e.preventDefault();
        const data = {
            pages: this.state.pages,
            location: this.state.location,
            type: this.state.type,
            minPrice: this.state.minPrice,
            maxPrice: this.state.maxPrice,
            title: this.state.title,
            description: this.state.description
        };
        await axios.post('http://localhost:8000/runProgram/',data)
        console.log("Form Submitted: ", this.state);
    };



    render() {
        return (
            <div className="search-container">
                <h1 className="search-header">Search Form</h1>
                <form onSubmit={this.handleSubmit} className="search-form">
                    <div className="form-columns">
                        <div className="form-column">
                            <div className="form-group">
                                <label htmlFor="title" className="form-label">Title:</label>
                                <input 
                                    type="text" 
                                    id="title" 
                                    name="title" 
                                    className="form-input"
                                    value={this.state.title} 
                                    onChange={this.handleChange} 
                                    required 
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="minPrice" className="form-label">Minimum Price:</label>
                                <input 
                                    type="number" 
                                    id="minPrice" 
                                    name="minPrice" 
                                    className="form-input"
                                    value={this.state.minPrice} 
                                    onChange={this.handleChange} 
                                    required 
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="type" className="form-label">Type:</label>
                                <select className='form-input' onChange={this.handleChange} name="type"  id="">
                                    {this.state.typeList.map( type => {
                                        return(
                                            <option>{type[1]}</option>
                                        )
                                    })}
                                </select>
                            </div>
                        </div>
                        <div className="form-column">
                            <div className="form-group">
                                <label htmlFor="location" className="form-label">Location:</label>
                                <select className="form-input" onChange={this.handleChange} name="location"  id="">
                                    {this.state.locationList.map( type => {
                                        return(
                                            <option>{type[1]}, {type[2]}</option>
                                        )
                                    })}
                                </select>
                            </div>
                            <div className="form-group">
                                <label htmlFor="maxPrice" className="form-label">Maximum Price:</label>
                                <input 
                                    type="number" 
                                    id="maxPrice" 
                                    name="maxPrice" 
                                    className="form-input"
                                    value={this.state.maxPrice} 
                                    onChange={this.handleChange} 
                                    required 
                                />
                            </div>
                            <div className="form-group">
                                <label htmlFor="pages" className="form-label">Pages:</label>
                                <input 
                                    type="number" 
                                    id="pages" 
                                    name="pages" 
                                    className="form-input"
                                    value={this.state.pages} 
                                    onChange={this.handleChange} 
                                    required 
                                />
                            </div>
                        </div>
                    </div>
                    <div className="form-group">
                        <label htmlFor="description" className="form-label">Description:</label>
                        <textarea 
                            id="description" 
                            name="description" 
                            className="form-textarea"
                            value={this.state.description} 
                            onChange={this.handleChange} 
                            required 
                        ></textarea>
                    </div>
                    <button type="submit" className="submit-button" onClick={this.handleSubmit}>Submit</button>
                </form>
            </div>
        );
    }
}

export default Search;
