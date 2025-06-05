import React from 'react';
import './CardButton.css'; // Assuming you will create a CSS file for styling

const CardButton = ({ imagePath, text, onClick }) => {
    return (
        <div className="card-button" onClick={onClick}>
            <img src={imagePath} alt={text} className="card-button-icon" />
            <span className="card-button-text">{text}</span>
        </div>
    );
};

export default CardButton;