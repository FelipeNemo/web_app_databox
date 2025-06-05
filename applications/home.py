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

# Adicione logo após o aplicar_css_personalizado() ou no início da função mostrar_home()



st.markdown("""
    <div style="position: fixed; top: 60px; right: 32px; z-index: 9999;">
        <a href="?login=1">
            <button style="background: #FFD60A; color: #22223b; border: none; border-radius: 6px; padding: 8px 20px; font-size: 16px; font-weight: bold; cursor: pointer;">
                Login
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# Detecta o clique no botão HTML via query string
if st.query_params.get("login") == "1":
    st.session_state.pagina = 'login'
    st.query_params.clear()
    st.rerun()

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
    logo_databox = "data/logo_databox.png"
    icon_data = "data/data_icon.png"  
    icon_ia = "data/ia_icon.png"  
    icon_dash = "data/dash_icon.png"  

    if os.path.exists(logo_databox):
        with open(logo_databox, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <div style='display: flex; align-items: center; justify-content: center; gap: 20px; background-color: white; padding: 20px; border-radius: 16px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4); margin-bottom: 30px;'>
            <img src="data:image/png;base64,{logo_base64}" style="max-width: 200px; height: auto; border-radius: 12px;" />
            <h1 style='color: #FFD60A; margin: 0; font-size: 56px;'>DATABOX</h1>
        </div>
        """, unsafe_allow_html=True)

        # Carregar ícones em base64
    def img_to_base64(path):
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        return ""

    icon_data_b64 = img_to_base64(icon_data)
    icon_ia_b64 = img_to_base64(icon_ia)
    icon_dash_b64 = img_to_base64(icon_dash)

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
    

    # --- Botões centralizados com HTML
    st.markdown(f"""
    <div style="display: flex; justify-content: center; gap: 100px; margin-bottom: 32px;">
        <a href='#secao1' style="text-align: center;">
            <img src="data:image/png;base64,{icon_data_b64}" style="width:280px; height:280px; display:block; margin:auto;"/>
            <button class='botao-scroll'>Mapeie seu cenário atual</button>
        </a>
        <a href='#secao2' style="text-align: center;">
            <img src="data:image/png;base64,{icon_ia_b64}" style="width:280px; height:280px; display:block; margin:auto;"/>
            <button class='botao-scroll'>IA para escalar suas decisões</button>
        </a>
        <a href='#secao3' style="text-align: center;">
            <img src="data:image/png;base64,{icon_dash_b64}" style="width:280px; height:280px; display:block; margin:auto;"/>
            <button class='botao-scroll'>Visualize suas métricas</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: black;'>Pronto para começar?</h3>", unsafe_allow_html=True)

    # Botão HTML centralizado
    st.markdown("""
    <div style="display: flex; justify-content: center; margin-bottom: 32px;">
        <a href="?perguntas=1">
            <button class="botao-scroll" style="min-width:320px;">Quero responder algumas perguntas</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Detecta o clique no botão HTML via query string
    if st.query_params.get("perguntas") == "1": #O clique no botão adiciona ?perguntas=1 na URL
         # O Python detecta esse parâmetro e faz a navegação para o formulário.
        st.session_state.pagina = 'perguntas'
        st.query_params.clear()
        st.rerun()

    st.markdown("---")

    # Centralizando o botão com HTML e usando o botão do Streamlit para navegação
    #st.markdown('<div style="display: flex; justify-content: center; margin-bottom: 32px;">', unsafe_allow_html=True)
    #if st.button("Quero responder algumas perguntas", key="perguntas"):
    #    st.session_state.pagina = 'perguntas'
    #    st.rerun()
    #st.markdown('</div>', unsafe_allow_html=True)



    # --- Seção 1
    st.markdown("<div id='secao1' style='scroll-margin-top: 500px;'></div>", unsafe_allow_html=True)
    #st.markdown("<div style='margin-top: 80px;' id='secao1'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>Mapeie seu cenário atual e encontre oportunidades</h2>", unsafe_allow_html=True)
    #st.header("Mapeie seu cenário atual e encontre oportunidades")
    st.write("""Com nossa análise detalhada, você obtém um panorama completo do seu negócio," \
             "identificando pontos fortes, fraquezas e novas oportunidades de crescimento. \
             Utilizamos dados reais e atualizados para mostrar onde você está e o que pode ser melhorado, ajudando a tomar decisões estratégicas \
             com segurança.
             """)

    # --- Seção 2
    st.markdown("<div id='secao2' style='scroll-margin-top: 500px;'></div>", unsafe_allow_html=True)
    #st.markdown("<div style='margin-top: 80px;' id='secao2'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: white;'>Use IA para escalar suas decisões</h2>", unsafe_allow_html=True)
    #st.header("Use IA para escalar suas decisões")
    st.write("""Aproveite o poder da inteligência artificial para automatizar análises complexas e prever tendências do seu mercado. 
                Nossa plataforma ajuda você a otimizar campanhas, reduzir custos e aumentar resultados com recomendações personalizadas baseadas em dados e algoritmos avançados.
                """)

    # --- Seção 3
    st.markdown("<div id='secao3' style='scroll-margin-top: 500px;'></div>", unsafe_allow_html=True)
    #st.markdown("<div style='margin-top: 80px;' id='secao3'></div>", unsafe_allow_html=True)
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
#with st.sidebar:
    #if st.button("Login"):
        #st.session_state.pagina = 'login'

# Roteamento

if st.session_state.pagina == 'home':
    mostrar_home()

elif st.session_state.pagina == 'login':
    mostrar_login()

elif st.session_state.pagina == 'perguntas':
    mostrar_perguntas()
