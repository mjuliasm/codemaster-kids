import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Importar módulos
from modules.auth import UserAuth
from modules.gamification import Gamification
from modules.code_executor import CodeExecutor
from modules.ai_helper import AIHelper
from config.lessons import LESSONS

# Configuração da página
st.set_page_config(
    page_title="🚀 CodeMaster Kids",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    :root {
        --primary-color: #FF6B6B;
        --secondary-color: #4ECDC4;
        --success-color: #95E1D3;
        --warning-color: #FFE66D;
        --danger-color: #FF6B6B;
    }
    
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    
    .level-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    
    .achievement-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    
    .code-output {
        background: #1e1e1e;
        color: #00ff00;
        padding: 15px;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        font-size: 0.9em;
    }
    
    .error-box {
        background: #ffebee;
        color: #c62828;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #c62828;
    }
    
    .success-box {
        background: #e8f5e9;
        color: #2e7d32;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #2e7d32;
    }
    
    .progress-bar-custom {
        width: 100%;
        height: 30px;
        background: #e0e0e0;
        border-radius: 15px;
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session state
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'username' not in st.session_state:
    st.session_state.username = None
if 'ai_helper' not in st.session_state:
    st.session_state.ai_helper = AIHelper()
if 'auth' not in st.session_state:
    st.session_state.auth = UserAuth()

# ==================== FUNÇÕES AUXILIARES ====================

def show_header():
    """Mostra cabeçalho da aplicação"""
    st.markdown("""
    <div class="main-title">
        🚀 CodeMaster Kids
        <br>
        <small>Aprenda a programar de verdade!</small>
    </div>
    """, unsafe_allow_html=True)

def show_user_profile(user_info):
    """Mostra perfil do usuário"""
    if user_info:
        user_id, name, age, level, points, streak = user_info
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("👤 Nome", name)
        with col2:
            st.metric("🎂 Idade", f"{age} anos")
        with col3:
            st.metric("⭐ Pontos", points)
        with col4:
            st.metric("🔥 Streak", f"{streak} dias")
        
        # Mostrar nível atual
        level_info = Gamification.get_level_info(level)
        st.markdown(f"""
        <div class="level-badge">
            {level_info['name']}
        </div>
        """, unsafe_allow_html=True)
        
        # Barra de progresso até próximo nível
        if level < 5:
            next_level = level + 1
            progress = Gamification.calculate_progress(points, next_level)
            next_requirement = Gamification.LEVELS_INFO[next_level]["points_required"]
            
            st.write(f"Progresso para Nível {next_level}: {progress:.1f}%")
            st.progress(progress / 100)
            st.caption(f"Faltam {int(next_requirement - points)} pontos para o próximo nível!")

def show_lessons(level):
    """Mostra as aulas de um nível"""
    level_data = LESSONS.get(level)
    
    if not level_data:
        st.error("Nível não encontrado!")
        return
    
    st.subheader(f"📚 {level_data['name']}")
    
    for lesson in level_data['lessons']:
        with st.expander(f"Aula {lesson['id']}: {lesson['title']}"):
            st.write(lesson['description'])
            st.markdown(lesson['content'])
            
            # Botão para fazer o desafio
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"🎯 Fazer Desafio - Aula {lesson['id']}", 
                            key=f"challenge_{level}_{lesson['id']}"):
                    st.session_state.current_challenge = {
                        'level': level,
                        'lesson_id': lesson['id'],
                        'title': lesson['title'],
                        'description': lesson['challenge'],
                        'robotics': lesson['robotics']
                    }
                    st.rerun()
            
            with col2:
                if st.button(f"💡 Dica - Aula {lesson['id']}", 
                            key=f"hint_{level}_{lesson['id']}"):
                    hint = st.session_state.ai_helper.get_hint(
                        lesson['content'],
                        st.session_state.username
                    )
                    st.info(f"💡 Dica: {hint}")

def show_code_editor(challenge):
    """Mostra o editor de código para um desafio"""
    st.subheader(f"🎯 {challenge['title']}")
    st.write(f"**Desafio**: {challenge['description']}")
    st.info(f"🤖 **Robótica**: {challenge['robotics']}")
    
    # Editor de código
    code = st.text_area(
        "Escreva seu código Python aqui:",
        height=300,
        placeholder="# Escreva seu código aqui...\nprint('Olá, mundo!')"
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        execute_btn = st.button("▶️ Executar Código", key="execute_code")
    with col2:
        hint_btn = st.button("💡 Pedir Dica", key="get_hint")
    with col3:
        help_btn = st.button("🤖 Ajuda da IA", key="get_ai_help")
    
    # Executar código
    if execute_btn and code:
        is_valid, error_msg = CodeExecutor.validate_code(code)
        
        if not is_valid:
            st.error(f"⚠️ {error_msg}")
        else:
            with st.spinner("⏳ Executando código..."):
                result = CodeExecutor.execute(code, include_robotics=True)
            
            if result['success']:
                st.markdown("""
                <div class="success-box">
                    ✅ Código executado com sucesso!
                </div>
                """, unsafe_allow_html=True)
                
                if result['output']:
                    st.markdown("**Saída:**")
                    st.markdown(f"""
                    <div class="code-output">
                        {result['output']}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.caption(f"⏱️ Tempo: {result['execution_time']:.3f}s")
            else:
                st.markdown("""
                <div class="error-box">
                    ❌ Erro na execução
                </div>
                """, unsafe_allow_html=True)
                st.error(result['error'])
    
    # Pedir dica
    if hint_btn:
        with st.spinner("💭 Gerando dica..."):
            hint = st.session_state.ai_helper.get_hint(
                challenge['description'],
                st.session_state.username
            )
        st.info(f"💡 {hint}")
    
    # Ajuda da IA
    if help_btn:
        with st.spinner("🤖 Claude está pensando..."):
            explanation = st.session_state.ai_helper.get_explanation(
                challenge['title'].split(':')[-1].strip(),
                level="básico",
                student_name=st.session_state.username
            )
        st.markdown("### 🤖 Explicação da IA:")
        st.markdown(explanation)

def show_ai_chat():
    """Mostra o chat com assistente de IA"""
    st.subheader("🤖 Assistente de IA - Claude")
    st.write("Converse com Claude para tirar dúvidas sobre programação!")
    
    # Chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Mostrar histórico
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.chat_message("user").write(message['content'])
        else:
            st.chat_message("assistant").write(message['content'])
    
    # Input do usuário
    user_input = st.chat_input("Digite sua pergunta...")
    
    if user_input:
        # Adicionar mensagem do usuário
        st.session_state.chat_history.append({
            'role': 'user',
            'content': user_input
        })
        st.chat_message("user").write(user_input)
        
        # Gerar resposta
        with st.spinner("🤖 Claude está respondendo..."):
            response = st.session_state.ai_helper.chat(
                user_input,
                context="Estou aprendendo programação para crianças"
            )
        
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': response
        })
        st.chat_message("assistant").write(response)

def show_achievements(user_id):
    """Mostra conquistas do usuário"""
    st.subheader("🏆 Minhas Conquistas")
    
    user_achievements = st.session_state.auth.get_achievements(user_id)
    all_achievements = Gamification.get_all_achievements()
    
    cols = st.columns(2)
    col_idx = 0
    
    for achievement_id, achievement_info in all_achievements.items():
        with cols[col_idx % 2]:
            if achievement_id in user_achievements:
                st.markdown(f"""
                <div class="achievement-box">
                    {achievement_info['name']}
                    <br>
                    <small>{achievement_info['description']}</small>
                    <br>
                    <strong>+{achievement_info['points']} pontos</strong>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.info(f"""
                🔒 {achievement_info['name']}
                
                {achievement_info['description']}
                """)
        col_idx += 1

def show_dashboard():
    """Mostra dashboard principal"""
    user_info = st.session_state.auth.get_user(st.session_state.username)
    
    if user_info:
        show_user_profile(user_info)
        
        # Abas principais
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📚 Aulas",
            "🏆 Conquistas",
            "🤖 Assistente IA",
            "ℹ️ Sobre",
            "👤 Perfil"
        ])
        
        with tab1:
            st.subheader("Escolha um Nível")
            level_col = st.slider("Selecione o nível:", 1, 5, user_info[3])
            show_lessons(level_col)
        
        with tab2:
            show_achievements(user_info[0])
        
        with tab3:
            show_ai_chat()
        
        with tab4:
            st.markdown("""
            ## 🚀 CodeMaster Kids
            
            Uma plataforma educativa para aprender programação de verdade!
            
            ### ✨ Características:
            - 🐍 **Python**: Fundamentos até programação avançada
            - 🗂️ **SQL**: Bancos de dados e consultas
            - 🤖 **IA**: Machine Learning e automação
            - 🤖 **Robótica**: Integração com projetos práticos
            - 🎮 **Gamificação**: Ganhe pontos e desbloqueie níveis
            
            ### 📖 Estrutura do Curso:
            - **Nível 1**: Fundamentos Python
            - **Nível 2**: Python Intermediário
            - **Nível 3**: Algoritmos & Estruturas de Dados
            - **Nível 4**: SQL e Bancos de Dados
            - **Nível 5**: IA e Machine Learning
            
            Cada nível integra conceitos de robótica com exemplos práticos!
            """)
        
        with tab4:
            st.markdown(f"""
            ### Informações do Perfil
            - **Nome**: {user_info[1]}
            - **Idade**: {user_info[2]} anos
            - **Nível**: {user_info[3]}
            - **Pontos Totais**: {user_info[4]}
            - **Streak**: {user_info[5]} dias
            """)
            
            if st.button("🚪 Sair da Conta"):
                st.session_state.user_id = None
                st.session_state.username = None
                st.rerun()

# ==================== MAIN APP ====================

def main():
    show_header()
    
    # Se não está logado, mostrar tela de login/registro
    if not st.session_state.user_id:
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Registrar"])
        
        with tab1:
            st.subheader("Faça Login")
            username = st.text_input("Nome de usuário:")
            
            if st.button("Entrar"):
                if username:
                    user_info = st.session_state.auth.get_user(username)
                    if user_info:
                        st.session_state.user_id = user_info[0]
                        st.session_state.username = username
                        st.session_state.auth.update_login(username)
                        st.success(f"Bem-vindo de volta, {user_info[1]}! 🎉")
                        st.rerun()
                    else:
                        st.error("Usuário não encontrado!")
                else:
                    st.warning("Por favor, digite seu nome de usuário")
        
        with tab2:
            st.subheader("Crie sua Conta")
            new_username = st.text_input("Escolha um nome de usuário:")
            name = st.text_input("Seu nome completo:")
            age = st.number_input("Sua idade:", min_value=8, max_value=18, value=11)
            
            if st.button("Criar Conta"):
                if new_username and name and age:
                    user_id = st.session_state.auth.register_user(new_username, name, age)
                    if user_id:
                        st.session_state.user_id = user_id
                        st.session_state.username = new_username
                        st.success(f"Conta criada com sucesso! Bem-vindo, {name}! 🎉")
                        st.rerun()
                    else:
                        st.error("Nome de usuário já existe! Escolha outro.")
                else:
                    st.warning("Por favor, preencha todos os campos")
    else:
        # Dashboard do usuário logado
        show_dashboard()

if __name__ == "__main__":
    main()
