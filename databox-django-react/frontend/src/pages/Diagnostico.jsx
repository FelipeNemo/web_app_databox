import React from 'react';
import CardButton from '../components/CardButton';
import './styles/custom.css';

const Diagnostico = () => {
    return (
        <div className="diagnostico-container">
            <h1>Diagnóstico de Oportunidades</h1>
            <p>Página de diagnóstico. Em breve mais funcionalidades!</p>
            <div className="button-container">
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

export default Diagnostico;