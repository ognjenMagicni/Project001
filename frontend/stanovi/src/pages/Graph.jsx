import React from "react"
import axios from 'axios'
import {Link} from 'react-router-dom'

class Graph extends React.Component{
    constructor(props){
        super(props)
        this.state = {listProperties:[],maxSquare:0,minSquare:3000,maxPrice:0,minPrice:100000000,squareList:[],priceList:[],buttonActivated:false}
    }

    componentDidMount = () => {
        this.getAllProperties()
    }

    getAllProperties = async () => {
        let url = window.location.href
        let tokens = url.split("/")
        let id = tokens[tokens.length-1]
        let id_search = await axios.get(`http://localhost:5000/getAllProperties/${id}`)

        let id_property = await axios.get(`http://localhost:5000/getSearch/${id}`)
        this.setState({listProperties:id_search.data,minPrice:id_property.data[0][3],maxPrice:id_property.data[0][4],minSquare:id_property.data[0][5],maxSquare:id_property.data[0][6]})
        
        this.setState({squareList:this.getRangeForSquare(5,id_property.data[0][6],id_property.data[0][5])})

        this.setState({priceList:this.getRangeForPrice(5,id_property.data[0][4],id_property.data[0][3])})

    }

    getRangeForSquare = (numRange,maxValue,minValue) => {
        let i=0
        let range = []
        let diff = (maxValue-minValue)/numRange
        range.push(minValue)
        while(i<numRange-2){
            range.push(minValue+diff)
            diff = diff + diff
            i++
        }
        range.push(maxValue)
        return range
    }

    getRangeForPrice = (numRange,maxValue,minValue) => {
        let i=0
        let range = []
        let diff = (maxValue-minValue)/numRange
        range.push(maxValue)
        while(i<numRange-2){
            range.push(maxValue-diff)
            diff = diff + diff
            i++
        }
        range.push(minValue)
        return range
    }

    getProportionForPrice = (price) => {
        let calculation = (price-this.state.minPrice)/(this.state.maxPrice-this.state.minPrice)
        return 100-parseInt(calculation*100)+"%"
    }

    getProportionForSquare = (square) => {
        let calculation = (square-this.state.minSquare)/(this.state.maxSquare-this.state.minSquare)
        return calculation*100+"%"
    }

    buttonClick = () => {
        this.setState({buttonActivated:!this.state.buttonActivated})
    }

    updateOnOff = async (id) => {
        try{
            if(this.state.buttonActivated){
                await axios.put("http://localhost:5000/updateOnOff/"+id)
                console.log("done")
                this.getAllProperties()
            }
        }
        catch(error){
            console.log(error)
        }
    }

    render(){
        return (
            <div id="mainDiv1">
                <button id="removeButton" onClick={this.buttonClick}>{this.state.buttonActivated ? "Turn On" : "Turn Off"}</button>
                <div id="map_price">
                    <div id="price">
                        {this.state.priceList.map(element => {
                            return(
                                <p>{element}</p>
                            )
                        })}
                    </div>
                    <div id="map">

                        {this.state.listProperties.map(property => {
                            if(property[9]==0){
                                return(
                                    <a target="_blank" href={property[8]}><div onClick={() => this.updateOnOff(property[0])} style={{backgroundColor:"black",top:this.getProportionForPrice(property[4]),left:this.getProportionForSquare(property[3])}} className="el"></div></a>
                                )
                            }
                            else{
                                return(
                                    <a target="_blank" href={property[8]}><div onClick={() => this.updateOnOff(property[0])} style={{top:this.getProportionForPrice(property[4]),left:this.getProportionForSquare(property[3])}} className="el"></div></a>
                                )
                            }
                        })}
                    
                        
                    </div>
                </div>
                <div id="square">
                    {this.state.squareList.map(element => {
                        return(
                            <p>{element}</p>
                        )
                    })}
                </div> 
                
            </div>
        )
    }
}


export default Graph