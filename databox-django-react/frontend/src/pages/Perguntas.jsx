import React, { useState } from 'react';
import './styles/custom.css';
import CardButton from '../components/CardButton';

const Perguntas = () => {
    const [nome, setNome] = useState('');
    const [problema, setProblema] = useState('');
    const [email, setEmail] = useState('');

    const handleSubmit = () => {
        if (nome && problema && email) {
            // Logic to send data to the backend
            alert('✅ Suas respostas foram enviadas! Em breve entrarei em contato.');
            // Reset fields
            setNome('');
            setProblema('');
            setEmail('');
        } else {
            alert('⚠️ Por favor, preencha todos os campos.');
        }
    };

    return (
        <div className="container">
            <h1>🔎 Me diga o que está te travando</h1>
            <input
                type="text"
                placeholder="Qual seu nome?"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
            />
            <textarea
                placeholder="Qual é o principal desafio que você está enfrentando com dados?"
                value={problema}
                onChange={(e) => setProblema(e.target.value)}
            />
            <input
                type="email"
                placeholder="Qual seu email para resposta?"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />
            <button onClick={handleSubmit}>Enviar</button>
            <CardButton
                imagemPath="data/dash_icon.png"
                texto="⬅️ Voltar"
                destino="home"
                key="voltar_btn"
            />
        </div>
    );
};

export default Perguntas;