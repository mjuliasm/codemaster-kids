#!/usr/bin/env python3
"""
Setup script para CodeMaster Kids
Configura ambiente e banco de dados
"""

import os
import sys
import subprocess
from pathlib import Path

def create_directories():
    """Cria diretórios necessários"""
    print("📁 Criando estrutura de diretórios...")
    
    dirs = [
        'data',
        'modules',
        'config',
        'lessons',
        'lessons/level1_python',
        'lessons/level2_python',
        'lessons/level3_algorithms',
        'lessons/level4_sql',
        'lessons/level5_ai'
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    print("✅ Diretórios criados!")

def create_env_file():
    """Cria arquivo .env"""
    print("📝 Criando arquivo .env...")
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write('ANTHROPIC_API_KEY=sua_chave_aqui\n')
        print("✅ Arquivo .env criado!")
        print("⚠️  Por favor, adicione sua chave Anthropic ao arquivo .env")
    else:
        print("✅ Arquivo .env já existe!")

def install_dependencies():
    """Instala dependências"""
    print("📦 Instalando dependências...")
    
    try:
        # Atualizar pip
        print("  - Atualizando pip...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], 
                      check=True, capture_output=True)
        
        # Instalar requirements
        print("  - Instalando packages...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
                      check=True, capture_output=True)
        
        print("✅ Dependências instaladas!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar: {e}")
        return False

def initialize_database():
    """Inicializa banco de dados"""
    print("🗂️ Inicializando banco de dados...")
    
    from modules.auth import UserAuth
    
    try:
        auth = UserAuth()
        print("✅ Banco de dados criado!")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def run_tests():
    """Executa testes básicos"""
    print("🧪 Executando testes...")
    
    try:
        # Testar imports
        print("  - Testando imports...")
        from modules.auth import UserAuth
        from modules.gamification import Gamification
        from modules.code_executor import CodeExecutor
        from modules.ai_helper import AIHelper
        from config.lessons import LESSONS
        
        print("  - Testando Code Executor...")
        result = CodeExecutor.execute("print('Hello, World!')")
        assert result['success'], "Erro ao executar código"
        
        print("  - Testando Gamification...")
        levels = Gamification.get_all_levels()
        assert len(levels) == 5, "Número de níveis incorreto"
        
        print("✅ Todos os testes passaram!")
        return True
    except Exception as e:
        print(f"❌ Erro nos testes: {e}")
        return False

def print_next_steps():
    """Mostra próximos passos"""
    print("\n" + "="*60)
    print("🎉 Setup Completo!")
    print("="*60)
    print("\n📚 Próximos Passos:\n")
    print("1. Edite o arquivo .env e adicione sua chave Anthropic")
    print("   ANTHROPIC_API_KEY=sua_chave_aqui")
    print()
    print("2. Execute a aplicação:")
    print("   streamlit run app.py")
    print()
    print("3. Abra o navegador e acesse:")
    print("   http://localhost:8501")
    print()
    print("4. Crie uma conta e comece a aprender!")
    print()
    print("="*60)

def main():
    print("🚀 CodeMaster Kids - Setup")
    print("="*60 + "\n")
    
    # Criar diretórios
    create_directories()
    
    # Criar arquivo .env
    create_env_file()
    
    # Instalar dependências
    if not install_dependencies():
        print("⚠️  Tente instalar manualmente: pip install -r requirements.txt")
        return
    
    # Inicializar banco de dados
    if not initialize_database():
        print("⚠️  Verifique o banco de dados manualmente")
        return
    
    # Executar testes
    if not run_tests():
        print("⚠️  Alguns testes falharam, mas você pode tentar executar a app")
    
    # Mostrar próximos passos
    print_next_steps()

if __name__ == '__main__':
    main()
