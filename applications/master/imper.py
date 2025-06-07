import streamlit as st

""" Gerencia o "Imperador" (usuário)"""



def pagina_master():
    # Lê e injeta o CSS diretamente para garantir aplicação do efeito fosco
    with open("styles/master_frosted.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.title("Área Master")
    # Exemplo de instância do Imperador (pode ser substituído por dados reais do usuário logado)
    imperador = Imperador("Imperador Exemplo")
    imperador.xp = 250
    imperador.nivel = 3
    imperador.moedas = 42
    imperador.badges = ["Primeiro Cliente", "5 Dias Seguidos"]
    imperador.quests_concluidas = ["Faculdade: Entreguei projeto", "Saúde: Meditei"]

    st.markdown(f"""
    <div style='text-align:center; margin-top:40px;'>
        <h2 style='color:#FFD60A;'>Bem-vindo, <b>{imperador.nome}</b>!</h2>
        <p style='font-size:20px; color:#333;'>Nível: <b>{imperador.nivel}</b> | XP: <b>{imperador.xp}</b> | Moedas: <b>{imperador.moedas}</b></p>
        <hr style='margin:32px 0;'>
        <p style='color:#888;'>Badges conquistados:</p>
        <ul style='font-size:18px; color:#555; text-align:left; display:inline-block;'>
            {''.join([f'<li>{badge}</li>' for badge in imperador.badges]) or '<li>Nenhuma badge ainda</li>'}
        </ul>
        <p style='color:#888; margin-top:24px;'>Quests concluídas:</p>
        <ul style='font-size:16px; color:#666; text-align:left; display:inline-block;'>
            {''.join([f'<li>{q}</li>' for q in imperador.quests_concluidas]) or '<li>Nenhuma quest concluída</li>'}
        </ul>
    </div>
    """, unsafe_allow_html=True)

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

class Imperador:
    def __init__(self, nome):
        self.nome = nome
        self.xp = 0
        self.nivel = 1
        self.badges = []
        self.moedas = 0
        self.quests_concluidas = []

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        if self.xp >= self.nivel * 100:  # Ex: 100 XP por nível
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def adicionar_badge(self, badge):
        if badge not in self.badges:
            self.badges.append(badge)

    def registrar_quest(self, quest_id):
        if quest_id not in self.quests_concluidas:
            self.quests_concluidas.append(quest_id)
