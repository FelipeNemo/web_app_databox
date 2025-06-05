import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import base64
import hashlib
from streamlit.components.v1 import html
from utils import aplicar_css_personalizado, enviar_email

# =====================
# CONFIGURAÇÃO INICIAL
# =====================
st.set_page_config(page_title="DATABOX", page_icon=" ", layout="wide")
load_dotenv()
aplicar_css_personalizado()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_APP = os.getenv("SENHA_APP")

# Estado inicial
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'

# Hash de senha
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =====================
# HOME
# =====================
def mostrar_home():
    logo_path = "data/logo_databox.png"
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <div style='display: flex; align-items: center; justify-content: center; gap: 20px; background-color: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4); margin-bottom: 30px;'>
            <img src="data:image/png;base64,{logo_base64}" style="max-width: 200px; height: auto; border-radius: 12px;" />
            <h1 style='color: #FFD60A; margin: 0; font-size: 56px;'>DATABOX</h1>
        </div>
        """, unsafe_allow_html=True)

    # --- Estilo dos botões (opcional)
    st.markdown("""
        <style>
            .botao-scroll {
                background-color: #008CBA;
                color: white;
                padding: 10px 20px;
                margin: 10px 0;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    # Subtítulo
    st.markdown("<h2 style='text-align: center; color: white;'>Transforme seu negócio com IA</h2>", unsafe_allow_html=True)
    

    # --- Botões que redirecionam para seções usando links HTML
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<a href='#secao1'><button class='botao-scroll'>Mapeie seu cenário atual e encontre oportunidades</button></a>", unsafe_allow_html=True)
    with col2:
        st.markdown("<a href='#secao2'><button class='botao-scroll'>Use IA para escalar suas decisões</button></a>", unsafe_allow_html=True)
    with col3:
        st.markdown("<a href='#secao3'><button class='botao-scroll'>Visualize suas métricas com clareza</button></a>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("\n")
    col4, col5, col6 = st.columns(3)
    st.markdown("<h3 style='text-align: center; color: black;'>Pronto para começar?</h3>", unsafe_allow_html=True)
    if col5.button("Quero responder algumas perguntas"):
        st.session_state.pagina = 'perguntas'
        st.rerun()

    # --- Seção 1
    st.markdown("<div style='margin-top: 300px;' id='secao1'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>Mapeie seu cenário atual e encontre oportunidades</h2>", unsafe_allow_html=True)
    #st.header("Mapeie seu cenário atual e encontre oportunidades")
    st.write("""Com nossa análise detalhada, você obtém um panorama completo do seu negócio," \
             "identificando pontos fortes, fraquezas e novas oportunidades de crescimento. \
             Utilizamos dados reais e atualizados para mostrar onde você está e o que pode ser melhorado, ajudando a tomar decisões estratégicas \
             com segurança.
             """)

    # --- Seção 2
    st.markdown("<div style='margin-top: 300px;' id='secao2'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>Use IA para escalar suas decisões</h2>", unsafe_allow_html=True)
    #st.header("Use IA para escalar suas decisões")
    st.write("""Aproveite o poder da inteligência artificial para automatizar análises complexas e prever tendências do seu mercado. 
                Nossa plataforma ajuda você a otimizar campanhas, reduzir custos e aumentar resultados com recomendações personalizadas baseadas em dados e algoritmos avançados.
                """)

    # --- Seção 3
    st.markdown("<div style='margin-top: 300px;' id='secao3'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>Visualize suas métricas com clareza</h2>", unsafe_allow_html=True)
    #st.header("Visualize suas métricas com clareza")
    st.write("""Transforme números e dados brutos em dashboards intuitivos e interativos. 
            Acompanhe em tempo real os principais indicadores do seu negócio, entenda o desempenho das suas estratégias 
            e tome decisões rápidas e embasadas para alcançar seus objetivos.
            """)



# =====================
# PERGUNTAS
# =====================
def mostrar_perguntas():
    st.title("🔎 Me diga o que está te travando")
    nome = st.text_input("Qual seu nome?")
    problema = st.text_area("Qual é o principal desafio que você está enfrentando com dados?")
    email = st.text_input("Qual seu email para resposta?")

    if st.button("Enviar"):
        if nome and problema and email:
            enviar_email(nome, problema, email)
            st.success("✅ Suas respostas foram enviadas! Em breve entrarei em contato.")
            st.balloons()
            st.session_state.pagina = 'home'
            st.rerun()
        else:
            st.warning("⚠️ Por favor, preencha todos os campos.")

    if st.button("⬅️ Voltar"):
        st.session_state.pagina = 'home'
        st.rerun()

def mostrar_login():
    st.title("🔐 Login")
    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if email == EMAIL_REMETENTE and hash_password(senha) == hash_password(SENHA_APP):
            st.session_state.pagina = 'home'
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("E-mail ou senha incorretos.")

    if st.button("⬅️ Voltar"):
        st.session_state.pagina = 'home'
        st.rerun()

# =====================
# SIDEBAR & ROTAS
# =====================
with st.sidebar:
    if st.button("Login"):
        st.session_state.pagina = 'login'

# Roteamento

if st.session_state.pagina == 'home':
    mostrar_home()

elif st.session_state.pagina == 'login':
    mostrar_login()

elif st.session_state.pagina == 'perguntas':
    mostrar_perguntas()
