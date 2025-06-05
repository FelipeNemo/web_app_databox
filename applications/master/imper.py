import streamlit as st


def pagina_master():
    st.title("Área Master")
    st.markdown(
        """
    <div style='text-align:center; margin-top:40px;'>
        <h2 style='color:#FFD60A;'>Bem-vindo à área exclusiva do master!</h2>
        <p style='font-size:20px; color:#333;'>Aqui você poderá acessar funcionalidades administrativas, dashboards, relatórios e muito mais.</p>
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
    """,
        unsafe_allow_html=True,
    )