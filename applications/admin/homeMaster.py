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
    st.markdown("<h2 style='text-align: center; color: white;'>Bem-vindo, Felipe</h2>", unsafe_allow_html=True)
    

    # 🔧 Carrega CSS, se existir
    try:
        with open("styles/master_frosted.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Estilo visual não encontrado.")

    #Carrega dados
    master = carregar_dados()

  # --- Blocos centralizados horizontalmente
    # Monta HTML com blocos
    colunas_html = f"""
    <div class="cards-container">
        <div class="frosted-box" style="width: 400px; height: 900px;">
            <h3 style="text-align:center;">Status</h3>
            <p><strong>Nível:</strong> {master.nivel}</p>
            <p><strong>XP:</strong> {master.xp}</p>
            <p><strong>Moedas:</strong> {master.moedas}</p>
            <p><strong>Emblemas:</strong></p>
            {"<ul>" + "".join(f"<li>{e}</li>" for e in master.emblemas) + "</ul>" if master.emblemas else "<em>Sem emblemas ainda.</em>"}
        </div>
        <div class="frosted-box" style="width: 400px; height: 900px;">
            <h3 style="text-align:center;">Menu</h3>
            <p style="text-align:center;"><em>Use os campos abaixo:</em></p>
        </div>
        <div class="frosted-box" style="width: 400px; height: 900px;">
            <h3 style="text-align:center;">Habilidades</h3>
            {("<ul>" + "".join(f"<li>{q}</li>" for q in master.quests_concluidas) + "</ul>") if master.quests_concluidas else "<em>Nenhuma missão concluída.</em>"}
        </div>
    </div>
    """


    # Renderiza HTML com permissão
    st.markdown(colunas_html, unsafe_allow_html=True)

    st.markdown("""
    <div class="frosted-box" style="margin-top:32px;">
        <hr style='margin:32px 0;'>
        <p style='color:#888;'>Menu de funcionalidades futuras:</p>
        <ul style='font-size:18px; color:#555; text-align:left; display:inline-block;'>
            <li>Gestão de usuários</li>
            <li>Dashboards avançados</li>
            <li>Relatórios customizados</li>
            <li>Configurações do sistema</li>
            <li>Integração com IA</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

