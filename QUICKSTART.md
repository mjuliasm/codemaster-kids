#!/usr/bin/env python3
"""
QUICKSTART - CodeMaster Kids 🚀
Comece em 5 minutos!
"""

print("""
╔═══════════════════════════════════════════════════════════════╗
║         🚀 CodeMaster Kids - Início Rápido                   ║
║    Plataforma de Aprendizado de Programação para Crianças    ║
╚═══════════════════════════════════════════════════════════════╝

📋 O QUE É?
===========
CodeMaster Kids é uma plataforma gamificada para ensinar 
programação REAL a crianças de 11 anos:
  • Python (fundamentos até avançado)
  • SQL e bancos de dados
  • Inteligência Artificial
  • Robótica integrada
  • Desafios e conquistas


🚀 COMEÇAR LOCALMENTE (5 MINUTOS)
===================================

PASSO 1: Clonar o Repositório
$ git clone https://github.com/seu-usuario/codemaster-kids.git
$ cd codemaster-kids

PASSO 2: Criar Ambiente Virtual
$ python -m venv venv
$ source venv/bin/activate  # No Windows: venv\\Scripts\\activate

PASSO 3: Instalar Dependências
$ pip install -r requirements.txt

PASSO 4: Configurar API Key
$ cp .env.example .env
$ # Edite .env e adicione sua chave Anthropic
$ nano .env
   ANTHROPIC_API_KEY=sk-...seu-api-key...

PASSO 5: Executar o App
$ streamlit run app.py

PRONTO! 🎉
Abra seu navegador em http://localhost:8501


☁️ DEPLOY NO STREAMLIT CLOUD (10 MINUTOS)
===========================================

1. Faça push do código para GitHub:
   $ git add .
   $ git commit -m "Initial commit"
   $ git push origin main

2. Acesse: https://share.streamlit.io/

3. Clique em "New app" e preencha:
   - Repository: seu-usuario/codemaster-kids
   - Branch: main
   - Main file: app.py

4. Clique "Deploy"

5. Após deploy, vá para "Secrets" e adicione:
   ANTHROPIC_API_KEY=sua_chave_aqui

6. Seu app estará disponível em: 
   https://seu-app-name.streamlit.app


📁 ESTRUTURA DO PROJETO
========================

codemaster-kids/
├── app.py                  # Aplicação principal
├── modules/                # Módulos Python
│   ├── auth.py            # Usuários e autenticação
│   ├── gamification.py     # Sistema de pontos/níveis
│   ├── code_executor.py    # Execução segura de código
│   └── ai_helper.py        # Integração com Claude
├── config/                 # Configurações
│   ├── lessons.py          # 5 níveis × 5 aulas
│   └── challenges.py       # Desafios extras
├── requirements.txt        # Dependências
├── README.md              # Documentação completa
├── GUIDE.md               # Guia de uso
├── DEPLOY.md              # Instruções de deploy
├── CONTRIBUTING.md        # Como contribuir
└── ARCHITECTURE.md        # Arquitetura técnica


📚 5 NÍVEIS DE APRENDIZAGEM
=============================

🟢 NÍVEL 1: Fundamentos Python (Semanas 1-3)
- Variáveis e tipos de dados
- Operações matemáticas
- Estruturas if/else
- Loops (for)
- Funções básicas
- 🤖 Robótica: Controle de LEDs

🟡 NÍVEL 2: Python Intermediário (Semanas 4-6)
- Listas e dicionários
- Loops while
- Manipulação de strings
- Tratamento de erros
- 🤖 Robótica: Sensores

🟠 NÍVEL 3: Algoritmos & Estruturas de Dados (Semanas 7-9)
- Busca e ordenação
- Complexidade de algoritmos
- Recursão
- 🤖 Robótica: Navegação autônoma

🔴 NÍVEL 4: Banco de Dados com SQL (Semanas 10-12)
- SELECT, INSERT, UPDATE, DELETE
- JOINs e queries complexas
- Design de banco de dados
- 🤖 Robótica: Armazenar dados

🟣 NÍVEL 5: IA e Machine Learning (Semanas 13-15)
- Introdução a IA
- Datasets e treinamento
- Modelos de previsão
- 🤖 Robótica: IA em robôs autônomos


🎮 COMO FUNCIONA
==================

1. CRIAR CONTA
   Simples: nome de usuário, nome real, idade

2. ESCOLHER NÍVEL
   Comece no Nível 1, progredindo conforme completa desafios

3. APRENDER
   Leia aulas estruturadas com exemplos práticos

4. FAZER DESAFIOS
   Execute código Python com segurança em sandbox

5. GANHAR PONTOS
   Complete desafios → ganhe pontos → desbloqueie níveis

6. CONQUISTAR BADGES
   Conquistas especiais ao atingir marcos

7. PEDIR AJUDA
   Chat com IA Claude para tirar dúvidas


✨ FUNCIONALIDADES
====================

✅ Editor de Código com Syntax Highlighting
✅ Execução Segura de Código Python
✅ Assistente de IA (Claude API)
✅ 25 Aulas Estruturadas
✅ Desafios Progressivos
✅ Sistema de Pontos e Níveis
✅ Badges e Conquistas
✅ Chat Educativo
✅ Integração com Robótica
✅ Banco de Dados SQLite
✅ Interface Gamificada


🆘 TROUBLESHOOTING
====================

"Erro ao instalar dependências"
→ Certifique-se de estar em venv virtual
→ Tente: pip install --upgrade pip

"Erro ANTHROPIC_API_KEY"
→ Verifique se adicionou a chave em .env
→ A chave deve começar com "sk-"

"Código não executa"
→ Verifique sintaxe (parênteses, dois-pontos)
→ Leia mensagem de erro
→ Use assistente de IA para debugar

"App não carrega"
→ Aguarde 2-3 minutos após push
→ Verifique status em Streamlit Cloud
→ Veja logs de erro


📚 DOCUMENTAÇÃO ADICIONAL
===========================

README.md              → Documentação completa
GUIDE.md              → Como usar a plataforma
DEPLOY.md             → Deploy no Streamlit Cloud
CONTRIBUTING.md       → Como contribuir
ARCHITECTURE.md       → Arquitetura técnica


💡 PRÓXIMOS PASSOS
====================

PARA USAR:
1. Clonar repositório
2. Instalar dependências
3. Adicionar API key
4. Executar: streamlit run app.py

PARA FAZER DEPLOY:
1. Fazer push para GitHub
2. Conectar em share.streamlit.io
3. Adicionar secret com API key
4. Acessar URL pública

PARA CONTRIBUIR:
1. Fork o repositório
2. Criar nova branch
3. Fazer mudanças
4. Abrir Pull Request


🎓 EXEMPLO DE PRIMEIRA AULA
=============================

Ao fazer login, a criança verá:

  📚 Aula 1: Variáveis e Tipos de Dados
  
  Conteúdo:
  "Uma variável é como uma caixa que guarda informações..."
  
  Exemplo:
  ```python
  nome = "João"
  idade = 11
  print(f"Olá, meu nome é {nome}")
  ```
  
  Desafio:
  "Crie variáveis com seu nome, idade e altura"
  
  [▶️ Executar] [💡 Dica] [🤖 Ajuda IA]


🤖 INTEGRAÇÃO COM ROBÓTICA
===========================

Cada aula mostra como o conceito aplica-se em robótica real:

Nível 1 - LEDs:
  ligar_led(LED_VERMELHO)
  desligar_led(LED_VERMELHO)

Nível 2 - Sensores:
  leitura = ler_sensor(SENSOR_DISTANCIA)

Nível 3 - Navegação:
  navegar_labirinto(mapa)

Nível 4 - Armazenar:
  INSERT INTO leituras VALUES (...)

Nível 5 - IA:
  modelo.prever(novo_dado)


⭐ PONTUAÇÃO & GAMIFICAÇÃO
=============================

Pontos por atividade:
- Primeiro código: 50 pts
- Aula completada: 100 pts
- Desafio concluído: 50-200 pts
- Conquista desbloqueada: +pts variável

Níveis desbloqueados por pontos:
- Nível 1: 0+ pontos
- Nível 2: 500+ pontos
- Nível 3: 1200+ pontos
- Nível 4: 2000+ pontos
- Nível 5: 3000+ pontos

Badges:
- 👶 Primeiro Código
- 🐍 Mestre em Python
- 🧙 Assistente SQL
- 🤖 Engenheiro de Robótica
- ⚔️ Guerreiro do Código
- ... e mais!


🚀 COMEÇAR AGORA!
==================

$ git clone https://github.com/seu-usuario/codemaster-kids.git
$ cd codemaster-kids
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py

Abra: http://localhost:8501


📧 DÚVIDAS?
===========

- Issues: https://github.com/seu-usuario/codemaster-kids/issues
- Discussions: https://github.com/seu-usuario/codemaster-kids/discussions
- Email: seu-email@example.com


═══════════════════════════════════════════════════════════════

Divirta-se aprendendo programação! 🚀
Crianças programam melhor quando se divertem!

═══════════════════════════════════════════════════════════════
""")

if __name__ == "__main__":
    input("\\nPressione Enter para continuar...")
