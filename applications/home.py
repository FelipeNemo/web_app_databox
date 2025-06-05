import streamlit as st
import os
from utils import *
from dotenv import load_dotenv
from PIL import Image
import base64

# Adicionando hash para simular autenticação simples
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# PRIMEIRA COISA
st.set_page_config(page_title="DATABOX", page_icon=" ", layout="wide")

# Carregar logo
logo_path = "data/logo_databox.png"
logo = Image.open(logo_path) if os.path.exists(logo_path) else None

# Aplicar CSS personalizado e Bootstrap CDN
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">', unsafe_allow_html=True)
aplicar_css_personalizado()

# Carregar variáveis do .env
load_dotenv()
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_APP = os.getenv("SENHA_APP")

# Iniciar a session_state
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'
if 'logado' not in st.session_state:
    st.session_state.logado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = ''

# =============================
# Função para exibir perguntas
# =============================
def mostrar_home():
    with st.container():
        if logo:
            with open(logo_path, "rb") as f:
                logo_base64 = base64.b64encode(f.read()).decode()

            st.markdown(f"""
            <div style='display: flex; align-items: center; justify-content: center; gap: 20px; width: 100%; background-color: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4); margin-bottom: 30px;'>
                <img src="data:image/png;base64,{logo_base64}" style="max-width: 200px; height: auto; border-radius: 12px; image-rendering: auto;" />
                <h1 style='color: #FFD60A; margin: 0; font-size: 56px; font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", sans-serif; font-weight: 700;'>DATABOX</h1>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>Transforme seu negócio com IA</h2>", unsafe_allow_html=True)

    def card_botao(imagem_path, texto, destino):
        with open(imagem_path, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
            <div class="d-flex flex-column align-items-center mt-3">
                <a href="/?page={destino}" style="text-decoration: none;">
                    <div class="shadow p-2 bg-white rounded-4" style="transition: box-shadow 0.3s;">
                        <img src="data:image/png;base64,{img_base64}" width="220px" style="border-radius: 12px;" />
                        <p class="fw-bold mt-2" style="color: black; width: 220px;">{texto}</p>
                    </div>
                </a>
            </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        card_botao("data/data_icon.png", "Mapeie seu cenário atual e encontre oportunidades.", "diagnostico")
    with col2:
        card_botao("data/ia_icon.png", "Use IA para escalar suas decisões.", "estrategias")
    with col3:
        card_botao("data/dash_icon.png", "Visualize suas métricas com clareza.", "dashboards")

    # Detectar clique via URL
    page = st.query_params.get("page", None)
    if page:
        st.session_state.pagina = page
        st.query_params.clear()
        st.rerun()

    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: black;'>Pronto para começar?</h3>", unsafe_allow_html=True)
    st.markdown(
        '''<div class="d-flex justify-content-center align-items-center" style="height: 80px;">
            <button class="btn btn-warning btn-lg fw-bold" style="background-color: #FFD60A; color: #1E1E1E; border-radius: 16px; border: none;" onclick="window.location.href='/?page=perguntas'">Quero responder algumas perguntas</button>
        </div>''', unsafe_allow_html=True)
    if st.button("Quero responder algumas perguntas", key="perguntas_btn_streamlit"):
        st.session_state.pagina = 'perguntas'
        st.rerun()

# Novas páginas para cada ícone

def mostrar_diagnostico():
    st.title("Diagnóstico de Oportunidades")
    st.info("Página de diagnóstico. Em breve mais funcionalidades!")
    if st.button("⬅️ Voltar"):
        st.session_state.pagina = 'home'
        st.rerun()

def mostrar_estrategias():
    st.title("Estratégias com IA")
    st.info("Página de estratégias. Em breve mais funcionalidades!")
    if st.button("⬅️ Voltar"):
        st.session_state.pagina = 'home'
        st.rerun()

def mostrar_dashboards():
    st.title("Dashboards e Métricas")
    st.info("Página de dashboards. Em breve mais funcionalidades!")
    if st.button("⬅️ Voltar"):
        st.session_state.pagina = 'home'
        st.rerun()

# Página de login/logout

def mostrar_login():
    st.title("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        # Usuário e senha fixos para exemplo
        if usuario == "admin" and hash_password(senha) == hash_password("admin123"):
            st.session_state.logado = True
            st.session_state.usuario = usuario
            st.session_state.pagina = 'chatgpt'
            st.success("Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
    if st.button("⬅️ Voltar"):
        st.session_state.pagina = 'home'
        st.rerun()

def mostrar_chatgpt():
    st.title("ChatGPT via API")
    st.info("Aqui você poderá conversar com o ChatGPT (integração futura)")
    if st.button("Sair"):
        st.session_state.logado = False
        st.session_state.usuario = ''
        st.session_state.pagina = 'home'
        st.rerun()

# Função para exibir perguntas
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



# =============================
# Roteador de páginas
# =============================
# Menu superior
menu = ["Home", "Diagnóstico", "Estratégias", "Dashboards", "Login"]
menu_map = {
    "Home": "home",
    "Diagnóstico": "diagnostico",
    "Estratégias": "estrategias",
    "Dashboards": "dashboards",
    "Login": "login"
}

with st.sidebar:
    escolha = st.selectbox("Navegação", menu)
    st.session_state.pagina = menu_map[escolha]

# Roteamento
if st.session_state.pagina == 'home':
    mostrar_home()
elif st.session_state.pagina == 'perguntas':
    mostrar_perguntas()
elif st.session_state.pagina == 'diagnostico':
    mostrar_diagnostico()
elif st.session_state.pagina == 'estrategias':
    mostrar_estrategias()
elif st.session_state.pagina == 'dashboards':
    mostrar_dashboards()
elif st.session_state.pagina == 'login':
    mostrar_login()
elif st.session_state.pagina == 'chatgpt' and st.session_state.logado:
    mostrar_chatgpt()