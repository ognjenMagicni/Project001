import React, { useState } from "react";
import axios from 'axios'

const ConfirmDialog = ({id_search}) => {
  const [showConfirmation, setShowConfirmation] = useState(false);

  const handleDelete = async () => {
    await axios.delete(`http://localhost:8000/deleteSearch/${id_search}`)
    setShowConfirmation(false); // Close the confirmation dialog
    window.location.reload(true);
  };

  return (
    <div>
      <button className="action-button action-delete" onClick={() => setShowConfirmation(true)}>Delete</button>

      {showConfirmation && (
        <div
          style={{
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            backgroundColor: "#fff",
            padding: "20px",
            boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.1)",
            zIndex: 1000,
          }}
        >
          <p>Are you sure you want to delete?</p>
          <button className="action-button" onClick={handleDelete} style={{ marginRight: "10px" }}>
            Yes
          </button>
          <button className="action-button" onClick={() => setShowConfirmation(false)}>No</button>
        </div>
      )}
      {showConfirmation && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            backgroundColor: "rgba(0, 0, 0, 0.5)",
            zIndex: 999,
          }}
          onClick={() => setShowConfirmation(false)}
        />
      )}
    </div>
  );
};

export default ConfirmDialog;