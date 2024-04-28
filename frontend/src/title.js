import React from 'react';
import './TitleDisplay.css'

const TitleDisplay = () => {
  return (
    <div className="title-container">
      <h1>PaaruBUS</h1>
      <div className="bus-logo">
        <img className="logo-img" src="https://t3.ftcdn.net/jpg/05/71/69/10/360_F_571691018_GxAIRdpQ1wk38db2lYkWQEhxqalnBsL3.jpg" alt="Bus Logo" />
      </div>
    </div>
  );
}

export default TitleDisplay;
