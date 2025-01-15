import React from "react"
import axios from 'axios'
import {Link} from 'react-router-dom'
import '../css/Menu.css'

class Menu extends React.Component{
    constructor(props){
        super(props)
        this.state = {key:"value"}
    } 

    render(){
        return (
            <div className="home-buttons-container">
                <Link to='/compare' className='no-style-link'><button className="home-button">Compare Estates Markets</button></Link>
                <Link to='/search' className='no-style-link'><button className="home-button">Gather Properties</button></Link>
                <Link to='/list' className='no-style-link'><button className="home-button" >List of Estates Properties</button></Link>
            </div>
        );
    }
}

export default Menu