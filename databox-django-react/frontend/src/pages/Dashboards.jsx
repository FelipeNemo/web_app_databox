import React from 'react';
import CardButton from '../components/CardButton';
import './styles/custom.css';

const Dashboards = () => {
    return (
        <div className="dashboards-container">
            <h1 className="title">Dashboards e Métricas</h1>
            <p className="description">Visualize suas métricas com clareza.</p>
            <div className="card-buttons">
                <CardButton 
                    imagePath="/assets/data_icon.png" 
                    text="Mapeie seu cenário atual e encontre oportunidades." 
                    destination="diagnostico" 
                />
                <CardButton 
                    imagePath="/assets/ia_icon.png" 
                    text="Use IA para escalar suas decisões." 
                    destination="estrategias" 
                />
                <CardButton 
                    imagePath="/assets/dash_icon.png" 
                    text="Visualize suas métricas com clareza." 
                    destination="dashboards" 
                />
            </div>
        </div>
    );
};

export default Dashboards;