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
# Função para exibir perguntas
# =============================
def mostrar_home():
    with st.container():
        if logo:
            with open(logo_path, "rb") as f:
                logo_base64 = base64.b64encode(f.read()).decode()

            st.markdown(f"""
            <div style='
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 20px;
                width: 100%;
                background-color: white;
                padding: 20px;
                border-radius: 16px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
                margin-bottom: 30px;
            '>
                <img src="data:image/png;base64,{logo_base64}" 
                     style="max-width: 200px; height: auto; border-radius: 12px; image-rendering: auto;" />
                <h1 style='
                    color: #FFD60A;
                    margin: 0;
                    font-size: 56px;
                    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", sans-serif;
                    font-weight: 700;
                '>DATABOX</h1>
            </div>
            """, unsafe_allow_html=True)
        # Subtítulo
    st.markdown("<h2 style='text-align: center; color: white;'>Transforme seu negócio com IA</h2>", unsafe_allow_html=True)
    
    
    def card_botao(imagem_path, texto, destino):
        with open(imagem_path, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
            <div style="text-align: center; margin-top: 20px;">
                <a href="/?page={destino}" style="text-decoration: none;">
                    <div style="
                        display: inline-block;
                        padding: 10px;
                        border-radius: 12px;
                        background-color: white;
                        transition: background-color 0.3s;
                        border-radius: 16px;
                        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
                    " onmouseover="this.style.backgroundColor='#e0e0e0'" 
                    onmouseout="this.style.backgroundColor='#f0f0f0'">
                        <img src="data:image/png;base64,{img_base64}" width="220px" style="border-radius: 12px;" />
                        <p style="margin-top: 12px; color: black; font-weight: bold; width: 220px;">{texto}</p>
                    </div>
                </a>
            </div>
        """, unsafe_allow_html=True)


    # Layout com 3 colunas
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
    st.markdown("\n")
    col4, col5, col6 = st.columns(3)
    st.markdown("<h3 style='text-align: center; color: black;'>Pronto para começar?</h3>", unsafe_allow_html=True)
    if col5.button("Quero responder algumas perguntas"):
        st.session_state.pagina = 'perguntas'
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
if st.session_state.pagina == 'home':
    mostrar_home()
elif st.session_state.pagina == 'perguntas':
    mostrar_perguntas()