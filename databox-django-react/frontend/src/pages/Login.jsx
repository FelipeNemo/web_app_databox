import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import './Login.css'; // Assuming you have a separate CSS file for styling

const Login = () => {
    const [usuario, setUsuario] = useState('');
    const [senha, setSenha] = useState('');
    const history = useHistory();

    const handleLogin = () => {
        // Simulate a login process
        if (usuario === 'admin' && senha === 'admin123') {
            // Redirect to the home page on successful login
            history.push('/home');
        } else {
            alert('Usuário ou senha incorretos.');
        }
    };

    return (
        <div className="login-container">
            <h1>Login</h1>
            <input
                type="text"
                placeholder="Usuário"
                value={usuario}
                onChange={(e) => setUsuario(e.target.value)}
            />
            <input
                type="password"
                placeholder="Senha"
                value={senha}
                onChange={(e) => setSenha(e.target.value)}
            />
            <button onClick={handleLogin}>Entrar</button>
            <button onClick={() => history.push('/')}>⬅️ Voltar</button>
        </div>
    );
};

export default Login;