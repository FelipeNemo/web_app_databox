import React from 'react';
import './styles/custom.css';
import logo from '../assets/logo_databox.png';
import CardButton from '../components/CardButton';

const Home = () => {
    return (
        <div className="home-container">
            <div className="header">
                <img src={logo} alt="Databox Logo" className="logo" />
                <h1 className="title">DATABOX</h1>
            </div>
            <h2 className="subtitle">Transforme seu negócio com IA</h2>
            <div className="card-container">
                <CardButton 
                    imagePath="../assets/data_icon.png" 
                    text="Mapeie seu cenário atual e encontre oportunidades." 
                    destination="diagnostico" 
                    key="diagnostico_btn" 
                />
                <CardButton 
                    imagePath="../assets/ia_icon.png" 
                    text="Use IA para escalar suas decisões." 
                    destination="estrategias" 
                    key="estrategias_btn" 
                />
                <CardButton 
                    imagePath="../assets/dash_icon.png" 
                    text="Visualize suas métricas com clareza." 
                    destination="dashboards" 
                    key="dashboards_btn" 
                />
            </div>
            <h3 className="ready-text">Pronto para começar?</h3>
            <div className="button-container">
                <button className="questions-button" onClick={() => {/* Logic to navigate to perguntas */}}>
                    Quero responder algumas perguntas
                </button>
            </div>
        </div>
    );
};

export default Home;