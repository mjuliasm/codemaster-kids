import streamlit as st

st.set_page_config(
    page_title="🚀 CodeMaster Kids",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .feature-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
    🚀 CodeMaster Kids
    <br>
    <small>Aprenda Programação de Verdade!</small>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
    <h3>🐍 Python</h3>
    <p>Fundamentos até Programação Avançada</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    <h3>🗂️ SQL</h3>
    <p>Bancos de Dados e Consultas</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
    <h3>🤖 IA</h3>
    <p>Machine Learning e Automação</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.write("## 📚 5 Níveis de Aprendizado")

st.write("""
**🟢 Nível 1: Fundamentos Python**
- Variáveis e tipos de dados
- Estruturas de controle
- Funções básicas

**🟡 Nível 2: Python Intermediário**
- Listas e dicionários
- Manipulação de strings
- Tratamento de erros

**🟠 Nível 3: Algoritmos**
- Busca e ordenação
- Recursão
- Complexidade

**🔴 Nível 4: SQL**
- Banco de dados
- Queries complexas
- Design de dados

**🟣 Nível 5: IA**
- Machine Learning
- Modelos de previsão
- Automação inteligente
""")

st.markdown("---")

st.write("## 🎮 Como Funciona")

tab1, tab2, tab3 = st.tabs(["📖 Aprender", "🎯 Desafiar", "🏆 Ganhar Pontos"])

with tab1:
    st.write("""
    - Leia aulas estruturadas
    - Veja exemplos de código
    - Entenda conceitos passo a passo
    - Integração com robótica real
    """)

with tab2:
    st.write("""
    - Resolva exercícios práticos
    - Execute código Python
    - Receba feedback da IA
    - Melhore seu código
    """)

with tab3:
    st.write("""
    - Ganhe pontos por desafios
    - Desbloqueie novos níveis
    - Conquiste badges
    - Suba no ranking
    """)

st.markdown("---")

st.success("✅ Platform CodeMaster Kids está FUNCIONANDO!")
st.info("🚀 Em breve: Login, aulas completas e assistente de IA!")
st.write("© 2024 CodeMaster Kids - Todos os direitos reservados")
