import React from "react"
import axios from 'axios'
import {Link} from 'react-router-dom'

class Interface extends React.Component{
    constructor(props){
        super(props)
        this.state = {listSearch:[],typeList:[],locationList:[],inputFields:{}}
        
    }
 
    componentDidMount = () => {
        this.setState({inputFields:{maxPrice:-1,minPrice:-1,location:-1,type:-1,pages:-1,title:-1,description:-1}})
        this.getListSearch()
        this.getTypeList()
        this.getLocationList()
    }

    getListSearch = async () => {
        let res = await axios.get("http://localhost:5000/getAllSearches/")
        this.setState({listSearch:res.data})
    }

    getTypeList = async () => {
        let types = await axios.get("http://localhost:5000/getTypes/")
        this.setState({typeList:types.data})
    }

    getLocationList = async () => {
        let locations = await axios.get("http://localhost:5000/getLocations/")
        this.setState({locationList:locations.data})
    }

    extractDate(dateString) {
        // Create a Date object from the date string
        const date = new Date(dateString);
    
        // Extract the day, month, and year
        const day = date.getUTCDate();
        const month = date.getUTCMonth() + 1; // getUTCMonth() returns month index (0-11)
        const year = date.getUTCFullYear();
        const res = day+". "+month+". "+year
    
        return res
    }
    
    numberChange = (e) => {
        this.setState(prevState => ({
            inputFields:{...prevState.inputFields, [e.target.name]:e.target.value}
        }))
        console.log(this.state)
    }

    runProgram = async () => {
        let res = await axios.post("http://localhost:5000/runProgram/",
            this.state.inputFields)
    }

    render(){
        return (
            <div id="mainDiv">
                <div id="a" className="flexColumn">
                    <div className="inputField flexRow">
                        <p>Minimal price</p>
                        <input onChange={this.numberChange} name="minPrice" type="number" />
                    </div>
                    <div className="inputField  flexRow">
                        <p>Maximal price</p>
                        <input onChange={this.numberChange} name="maxPrice" type="number" />
                    </div>
                    <div className="inputField flexRow">
                        <p>Location</p>
                        <select onChange={this.numberChange} name="location"  id="">
                            {this.state.locationList.map( location => {
                                return(
                                    <option>{location[1]}</option>
                                )
                            })}
                        </select>
                    </div>
                    <div className="inputField flexRow">
                        <p>Type</p>
                        <select onChange={this.numberChange} name="type"  id="">
                            {this.state.typeList.map( type => {
                                return(
                                    <option>{type[1]}</option>
                                )
                            })}
                        </select>
                    </div>
                    <div className="inputField flexRow">
                        <p>Pages</p>
                        <input onChange={this.numberChange} name="pages" type="number" />
                    </div>
                    <div className="inputField flexRow">
                        <p>Title</p>
                        <input onChange={this.numberChange} name="title" type="text" />
                    </div>
                    <div className="inputField flexRow">
                        <p>Description</p>
                        <textarea onChange={this.numberChange} name="description" type="text" />
                    </div>
                    <button className='button' onClick={this.runProgram}>Run search</button>
                </div>
                <div id="b">
                    {this.state.listSearch.map(element => {
                        return(
                            <div className="element">
                                <p>{element[0]}</p>
                                <p>{element[1]}</p>
                                <p>{element[2]}</p>
                                <p>{element[3]}</p>
                                <p>{element[4]}</p>
                                <p>{this.extractDate(element[5])}</p>
                                <Link to={`/graph/${element[0]}`}><button className="button">Open</button></Link>
                            </div>
                        )
                    })}
                </div>
            </div>
        )
    }
}


export default Interface