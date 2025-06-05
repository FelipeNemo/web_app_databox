import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Diagnostico from './pages/Diagnostico';
import Estrategias from './pages/Estrategias';
import Dashboards from './pages/Dashboards';
import Login from './pages/Login';
import Perguntas from './pages/Perguntas';
import './styles/custom.css';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/" exact component={Home} />
                    <Route path="/diagnostico" component={Diagnostico} />
                    <Route path="/estrategias" component={Estrategias} />
                    <Route path="/dashboards" component={Dashboards} />
                    <Route path="/login" component={Login} />
                    <Route path="/perguntas" component={Perguntas} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;