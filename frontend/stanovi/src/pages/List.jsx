import React from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';
import ConfirmDialog from "./ConfirmDialog.jsx";
import '../css/List.css'

class List extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            listSearch: [],
        };
    }

    componentDidMount() {
        this.getListSearch();
    }

    getListSearch = async () => {
        let res = await axios.get("http://localhost:8000/getAllSearches/")
        this.setState({listSearch:res.data})
    }

    handleOpen = (id_search) => {
        this.getAnalytics(id_search)
    };

    getAnalytics = (id_search) => {
        axios.get(`http://localhost:8000/getAnalytics/${id_search}`)
    }


    handleDelete = async (id) => {
        axios.delete(`http://localhost:8000/deleteSearch/${id}`)
    };

    handleBuy = (id) => {
        alert(`Buy row with ID: ${id}`);
    };

    render() {
        const { rows } = this.state;
        return (
            <div className="list-container">
                
                <table className="list-table">
                    <thead className="list-table-header">
                        <tr>
                            <th>ID</th>
                            <th>Title</th>
                            <th>Minimal price</th>
                            <th>Maximal price</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.listSearch.map(row => {
                            return (
                            <tr className="list-table-row">
                                <td className="list-table-cell">{row[0]}</td>
                                <td className="list-table-cell">{row[1]}</td>
                                <td className="list-table-cell">{row[3]}</td>
                                <td className="list-table-cell">{row[4]}</td>
                                <td className="list-table-cell-buttons">
                                    <Link to={`/analytics/${row[0]}`}><button className="action-button action-open"onClick={() => this.handleOpen(row[0])}>Open</button></Link>
                                    <ConfirmDialog id_search = {row[0]}></ConfirmDialog>
                                    <Link to={`/filter/${row[0]}`}><button className="action-button action-buy">Buy</button></Link>
                                </td>
                            </tr>
                            )
                        })}
                    </tbody>
                </table>
            </div>
        );
    }
}

export default List;

