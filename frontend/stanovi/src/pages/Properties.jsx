import React from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';

class Properties extends React.Component {
    constructor(props) {
        super(props);
        this.state = { properties: [] };
    }

    render() {
        return (
            <div id="propertiesDiv">
                Properties Component
            </div>
        );
    }
}

export default Properties;
