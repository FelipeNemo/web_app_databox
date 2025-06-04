import streamlit as st
import os
from utils import *
from dotenv import load_dotenv
from PIL import Image
import base64

# PRIMEIRA COISA
st.set_page_config(page_title="DATABOX", page_icon=" ", layout="wide")

# Carregar logo
logo_path = "data/logo_databox.png"
logo = Image.open(logo_path) if os.path.exists(logo_path) else None

# Aplicar CSS personalizado
aplicar_css_personalizado()

# Carregar variáveis do .env
load_dotenv()
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_APP = os.getenv("SENHA_APP")

# Iniciar a session_state
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'



# =============================
# Função da tela inicial
# =============================
def mostrar_home():
        with st.container():
            if logo:
                logo_base64 = base64.b64encode(open(logo_path, "rb").read()).decode()
        st.markdown(f"""
        <div style='display: flex; align-items: center; gap: 20px;'>
            <img src="data:image/png;base64,{logo_base64}" width="80"/>
            <h1 style='color:#00ADB5; margin: 0;'>DATABOX</h1>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("Decisões que valem a pena")
        st.markdown("#### Ciência de dados para quem se cansou de errar.")

        st.markdown("""
        <p style='font-size:16px; line-height:1.6'>
        Durante muito tempo, tomei decisões no chute — na vida, nos projetos, nos negócios.<br>
        Erros que poderiam ter sido evitados com análise e estatística, mas que custaram caro.
        </p>
        <p style='font-size:16px; line-height:1.6'>
        Foi aí que percebi: <strong>dados não são só números — são uma direção</strong>.<br>
        Uma direção que aponta para a verdade. Nem sempre fácil de ser ouvida. Mas sempre procurada.
        </p>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Precisa de um modelo data-driven no seu negócio?")
        st.markdown("""
        -  Diagnóstico de dados  
        -  Estratégias com IA  
        -  Dashboards de performance
        """)

        st.markdown("---")
        st.subheader("Pronto para começar?")

        if st.button("Quero responder algumas perguntas"):
            st.session_state.pagina = 'perguntas'
            st.rerun()

# =============================
# Função para exibir perguntas
# =============================
def mostrar_home():
    with st.container():
        if logo:
            logo_base64 = base64.b64encode(open(logo_path, "rb").read()).decode()
            st.markdown(f"""
            <div style='
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 20px;
                width: 100%;
                background-color: rgba(0, 0, 0, 0.4);
                padding: 20px;
                border-radius: 16px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
                margin-bottom: 30px;
            '>
                <img src="data:image/png;base64,{logo_base64}" width="140" style="border-radius: 12px;" />
                <h1 style='
                    color: #00ADB5;
                    margin: 0;
                    font-size: 50px;
                    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", sans-serif;
                    font-weight: 700;
                '>DATABOX</h1>
            </div>
            """, unsafe_allow_html=True)

    st.subheader("Decisões que valem a pena")
    st.markdown("#### Ciência de dados para quem se cansou de errar.")

    st.markdown("""
    <p style='font-size:16px; line-height:1.6'>
    Durante muito tempo, tomei decisões no chute — na vida, nos projetos, nos negócios.<br>
    Erros que poderiam ter sido evitados com análise e estatística, mas que custaram caro.
    </p>
    <p style='font-size:16px; line-height:1.6'>
    Foi aí que percebi: <strong>dados não são só números — são uma direção</strong>.<br>
    Uma direção que aponta para a verdade. Nem sempre fácil de ser ouvida. Mas sempre procurada.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Precisa de um modelo data-driven no seu negócio?")
    st.markdown("""
    -  Diagnóstico de dados  
    -  Estratégias com IA  
    -  Dashboards de performance
    """)

    st.markdown("---")
    st.subheader("Pronto para começar?")

    if st.button("Quero responder algumas perguntas"):
        st.session_state.pagina = 'perguntas'
        st.rerun()

# def mostrar_home():
#     with st.container():
#         if logo:
#             logo_base64 = base64.b64encode(open(logo_path, "rb").read()).decode()
#         st.markdown(f"""
#         <div style='
#             display: flex; 
#             align-items: center; 
#             gap: 20px;
#             padding: 12px 24px;
#             background-color: rgba(0, 0, 0, 0.4);
#             backdrop-filter: blur(6px);
#             -webkit-backdrop-filter: blur(6px);
#             border-bottom: 1px solid rgba(255, 255, 255, 0.407);
#             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.946);
#             border-radius: 8px;
#             max-width: fit-content;
#             margin: 0 auto;  /* centraliza horizontalmente */
#         '>
#             <img src="data:image/png;base64,{logo_base64}" width="100" />
#             <h1 style='
#                 color: #FFD60A;
#                 margin: 0;
#                 font-size: 56px;
#                 font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", sans-serif;
#                 font-weight: 700;
#                 text-shadow: 0 0 8px rgba(255, 214, 10, 0.7);
#             '>DATABOX</h1>
#         </div>
#         """, unsafe_allow_html=True)
#
#         st.subheader("Decisões que valem a pena")
#         st.markdown("#### Ciência de dados para quem se cansou de errar.")
#
#         st.markdown("""
#         <p style='font-size:16px; line-height:1.6'>
#         Durante muito tempo, tomei decisões no chute — na vida, nos projetos, nos negócios.<br>
#         Erros que poderiam ter sido evitados com análise e estatística, mas que custaram caro.
#         </p>
#         <p style='font-size:16px; line-height:1.6'>
#         Foi aí que percebi: <strong>dados não são só números — são uma direção</strong>.<br>
#         Uma direção que aponta para a verdade. Nem sempre fácil de ser ouvida. Mas sempre procurada.
#         </p>
#         """, unsafe_allow_html=True)
#
#         st.markdown("---")
#         st.markdown("### Precisa de um modelo data-driven no seu negócio?")
#         st.markdown("""
#         -  Diagnóstico de dados  
#         -  Estratégias com IA  
#         -  Dashboards de performance
#         """)
#
#         st.markdown("---")
#         st.subheader("Pronto para começar?")
#
#         if st.button("Quero responder algumas perguntas"):
#             st.session_state.pagina = 'perguntas'
#             st.rerun()

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
if st.session_state.pagina == 'home':
    mostrar_home()
elif st.session_state.pagina == 'perguntas':
    mostrar_perguntas()
