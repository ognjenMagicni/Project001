import React from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';

class Compare extends React.Component {
    constructor(props) {
        super(props);
        this.state = { list: [] };
    }

    render() {
        return (
            <div id="listDiv">
                List Component
            </div>
        );
    }
}

export default Compare;
