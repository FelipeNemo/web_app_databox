import streamlit as st
import json
import os

class Master:
    def __init__(self, nome= "Felipe", xp=0, nivel=1, emblemas=None, moedas=0, quests_concluidas=None):
        self.nome = nome
        self.xp = xp
        self.nivel = nivel
        self.emblemas = emblemas if emblemas is not None else []
        self.moedas = moedas
        self.quests_concluidas = quests_concluidas if quests_concluidas is not None else []

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        if self.xp >= self.nivel * 100:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.xp = 0
        st.success(f"Subiu para o nível {self.nivel}!")

    def adicionar_emblema(self, emblema):
        if emblema not in self.emblemas:
            self.emblemas.append(emblema)

    def registrar_quest(self, quest_id):
        if quest_id not in self.quests_concluidas:
            self.quests_concluidas.append(quest_id)

    def to_dict(self):
        return {
            "nome": self.nome,
            "xp": self.xp,
            "nivel": self.nivel,
            "emblemas": self.emblemas,
            "moedas": self.moedas,
            "quests_concluidas": self.quests_concluidas
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data.get("nome", "Administrador"),
            xp=data.get("xp", 0),
            nivel=data.get("nivel", 1),
            emblemas=data.get("emblemas", []),
            moedas=data.get("moedas", 0),
            quests_concluidas=data.get("quests_concluidas", [])
        )

def carregar_dados(path='data/master.json'):
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
        return Master.from_dict(data)
    return Master("Administrador")  # padrão inicial

def salvar_dados(master, path='data/master.json'):
    with open(path, 'w') as f:
        json.dump(master.to_dict(), f, indent=4)

def pagina_master():
    st.title("Área Master")

    # 🔧 Carrega CSS, se existir
    try:
        with open("styles/master_frosted.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Estilo visual não encontrado.")

    # 🧠 Carrega dados do JSON ou inicia padrão
    master = carregar_dados()

    # 🧱 Interface com 3 colunas
    col1, col2, col3 = st.columns(3)

    # Coluna 1 – Habilidades
    with col1:
        st.subheader("Habilidades")
        st.metric("Nível", master.nivel)
        st.metric("XP", master.xp)
        st.metric("Moedas", master.moedas)

        st.markdown("**Habilidades**")
        if master.emblemas:
            for e in master.emblemas:
                st.markdown(f"- {e}")

    # 🧩 Coluna 2 – Menu
    with col2:
        st.subheader("Menu")

        xp_input = st.number_input("Ganhar XP", min_value=0, step=10)
        master.ganhar_xp(xp_input)
        quest_diaria = st.text_input("Notificação: Missão diária")
        master.registrar_quest(quest_diaria)
        novo_emblema = st.text_input("Notificação: Nova habilidade")
        master.adicionar_emblema(novo_emblema)
        nova_quest = st.text_input("Notificação: Nova missão")
        master.registrar_quest(nova_quest)
        

    # 📋 Coluna 3 – Status
    with col3:
        st.subheader("Status")
        if master.quests_concluidas:
            for q in master.quests_concluidas:
                st.markdown(f"- {q}")