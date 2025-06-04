import streamlit as st
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import pandas as pd
import os

def aplicar_css_personalizado(path_css="styles/style.css"):
    try:
        with open(path_css) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Arquivo CSS não encontrado: {path_css}")

def salvar_em_csv(nome, problema, email_usuario):
    resposta = {
        "nome": nome,
        "email": email_usuario,
        "problema": problema,
        "data_hora": datetime.now().strftime("%Y-%m-%d")

    }

    caminho = "data/respostas_formulario.csv"

    if os.path.exists(caminho):
        df = pd.read_csv(caminho)
        # converte o dict para DataFrame com uma linha
        nova_linha = pd.DataFrame([resposta])
        # concatena o DataFrame antigo com a nova linha
        df = pd.concat([df, nova_linha], ignore_index=True)
    else:
        df = pd.DataFrame([resposta])

    df.to_csv(caminho, index=False)

def enviar_email(nome, problema, email_usuario):
    salvar_em_csv(nome, problema, email_usuario)

    # 1. E-mail para você (Felipe)
    corpo_para_voce = f"""
    Nova resposta do formulário DATABOX:

    Nome: {nome}
    Email do usuário: {email_usuario}

    Desafio informado:
    {problema}
    """

    msg_para_voce = MIMEText(corpo_para_voce)
    msg_para_voce['Subject'] = '📩 Nova resposta recebida no DATABOX'
    msg_para_voce['From'] = 'felipedata20@gmail.com'
    msg_para_voce['To'] = 'felipedata20@gmail.com'

    # 2. E-mail de confirmação para o usuário
    corpo_para_usuario = f"""
    Olá {nome},

    Recebemos sua resposta no formulário da DATABOX.

    Obrigado por compartilhar seu desafio.  
    Seu perfil está em análise e entraremos em contato em breve.

    📊 Até já,  
    Feliper Augusto
    """

    msg_para_usuario = MIMEText(corpo_para_usuario)
    msg_para_usuario['Subject'] = '✅ Sua resposta foi recebida!'
    msg_para_usuario['From'] = 'felipedata20@gmail.com'
    msg_para_usuario['To'] = email_usuario

    # Enviar os dois e-mails
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
    SENHA_APP = os.getenv("SENHA_APP")
    # depois dentro da função enviar_email:
    server.login(EMAIL_REMETENTE, SENHA_APP)
    server.send_message(msg_para_voce)
    server.send_message(msg_para_usuario)

    server.quit()