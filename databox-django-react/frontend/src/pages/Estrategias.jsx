import React from 'react';
import CardButton from '../components/CardButton';
import './styles/custom.css';

const Estrategias = () => {
    return (
        <div className="container">
            <h1 className="title">Estratégias com IA</h1>
            <p className="description">Explore como utilizar inteligência artificial para escalar suas decisões.</p>
            <div className="button-container">
                <CardButton 
                    imagePath="assets/ia_icon.png" 
                    text="Use IA para escalar suas decisões." 
                    destination="estrategias" 
                    key="estrategias_btn" 
                />
                <CardButton 
                    imagePath="assets/data_icon.png" 
                    text="Mapeie seu cenário atual e encontre oportunidades." 
                    destination="diagnostico" 
                    key="diagnostico_btn" 
                />
                <CardButton 
                    imagePath="assets/dash_icon.png" 
                    text="Visualize suas métricas com clareza." 
                    destination="dashboards" 
                    key="dashboards_btn" 
                />
            </div>
        </div>
    );
};

export default Estrategias;