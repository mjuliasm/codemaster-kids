# 🏗️ Arquitetura Técnica - CodeMaster Kids

## Visão Geral

CodeMaster Kids é uma plataforma educativa web-based construída com:
- **Frontend**: Streamlit
- **Backend**: Python puro
- **Banco de Dados**: SQLite
- **IA**: Claude API (Anthropic)

## Fluxo da Aplicação

```
┌─────────────────────────────────────────┐
│     Usuário acessa streamlit.io         │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│      app.py (Interface Principal)       │
│  - Login/Registro                       │
│  - Dashboard do usuário                 │
│  - Renderização de aulas                │
└──────────┬──────────────────────────────┘
           │
      ┌────┴────┬───────────┬──────────────┬──────────────┐
      │          │           │              │              │
      ▼          ▼           ▼              ▼              ▼
┌──────────┐ ┌────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│   auth   │ │lessons │ │ AI helper│ │ Executor │ │ gamific. │
│   .py    │ │  .py   │ │   .py    │ │   .py    │ │   .py    │
└──────────┘ └────────┘ └──────────┘ └──────────┘ └──────────┘
      │          │           │              │              │
      └──────┬───┴─────┬─────┴──────┬───────┴────┬─────────┘
             │         │            │            │
             ▼         ▼            ▼            ▼
         ┌─────────────────────────────────────────┐
         │      modules/config/database            │
         │  - users.db (SQLite)                    │
         │  - user_progress                        │
         │  - achievements                         │
         └─────────────────────────────────────────┘
             │
             └──────────┬──────────────┐
                        │              │
                        ▼              ▼
                   ┌──────────┐   ┌──────────┐
                   │ Anthropic│   │  SQLite  │
                   │  API     │   │ Database │
                   └──────────┘   └──────────┘
```

## Estrutura de Arquivos

```
codemaster-kids/
├── app.py                           # Aplicação principal Streamlit
│   ├── show_header()               # UI do cabeçalho
│   ├── show_user_profile()         # Perfil do usuário
│   ├── show_lessons()              # Exibe aulas
│   ├── show_code_editor()          # Editor de código
│   ├── show_ai_chat()              # Chat com IA
│   ├── show_achievements()         # Conquistas
│   └── show_dashboard()            # Dashboard principal
│
├── modules/                         # Módulos Python reutilizáveis
│   ├── auth.py                     # Autenticação e gerenciamento de usuários
│   │   ├── UserAuth class
│   │   ├── register_user()
│   │   ├── get_user()
│   │   ├── add_points()
│   │   └── add_achievement()
│   │
│   ├── gamification.py             # Sistema de gamificação
│   │   ├── LEVELS_INFO            # 5 níveis progressivos
│   │   ├── ACHIEVEMENTS           # 8+ badges
│   │   ├── calculate_level_from_points()
│   │   └── calculate_progress()
│   │
│   ├── code_executor.py            # Sandbox para executar código
│   │   ├── ALLOWED_BUILTINS       # Funções permitidas
│   │   ├── ROBOTICS_NAMESPACE     # Variáveis de robótica
│   │   ├── execute()              # Executa código seguro
│   │   ├── validate_code()        # Valida antes de executar
│   │   └── format_output()        # Formata saída
│   │
│   └── ai_helper.py               # Integração com Claude API
│       ├── get_hint()              # Dica sem spoiler
│       ├── get_explanation()       # Explicação clara
│       ├── debug_code()            # Ajuda a debugar
│       ├── evaluate_code_quality() # Avalia código
│       ├── chat()                  # Conversa educativa
│       └── generate_challenge()    # Cria desafio
│
├── config/                          # Configurações
│   ├── lessons.py                  # 5 níveis × 5 aulas cada
│   │   └── LESSONS[nivel][aula]
│   │       ├── title
│   │       ├── description
│   │       ├── content (markdown)
│   │       ├── challenge
│   │       └── robotics
│   │
│   └── challenges.py               # Desafios extras
│       ├── EXTRA_CHALLENGES
│       └── PROJECT_IDEAS
│
├── data/                            # Dados do usuário (criado em runtime)
│   └── users.db                    # Banco de dados SQLite
│
├── requirements.txt                 # Dependências Python
├── setup.py                         # Script de configuração
├── .env.example                     # Template de variáveis
├── README.md                        # Documentação principal
├── GUIDE.md                         # Guia de uso
├── DEPLOY.md                        # Guia de deploy
├── LICENSE                          # MIT License
└── streamlit_config.toml           # Configuração Streamlit
```

## Banco de Dados

### Schema SQLite

```sql
-- Tabela de Usuários
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    created_at TIMESTAMP,
    current_level INTEGER DEFAULT 1,
    total_points INTEGER DEFAULT 0,
    streak INTEGER DEFAULT 0,
    last_login TIMESTAMP
);

-- Progresso do Usuário
CREATE TABLE user_progress (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    level INTEGER NOT NULL,
    lesson INTEGER NOT NULL,
    completed BOOLEAN DEFAULT 0,
    completed_at TIMESTAMP,
    points_earned INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Conquistas
CREATE TABLE achievements (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    achievement_name TEXT NOT NULL,
    earned_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## Sistema de Gamificação

### Níveis (5 total)

| Nível | Nome | Pontos | Aulas |
|-------|------|--------|-------|
| 1 | 🟢 Fundamentos Python | 0+ | 5 |
| 2 | 🟡 Python Intermediário | 500+ | 5 |
| 3 | 🟠 Algoritmos | 1200+ | 5 |
| 4 | 🔴 SQL | 2000+ | 5 |
| 5 | 🟣 IA | 3000+ | 5 |

### Conquistas (8 total)

- 👶 Primeiro Código (50 pts)
- 🎓 Graduado Nível 1 (200 pts)
- 🐍 Mestre em Python (300 pts)
- 🧙 Assistente SQL (300 pts)
- 🤖 Engenheiro de Robótica (250 pts)
- 🤖 Explorador de IA (500 pts)
- 🔥 100 Dias em Fogo (1000 pts)
- ⚔️ Guerreiro do Código (500 pts)

## Integração com IA (Claude)

### Fluxo de Requisição

```python
# 1. Usuário pede ajuda
user_input = "Como faço um loop?"

# 2. AIHelper prepara contexto
context = "Estou aprendendo Nível 1 - Fundamentos Python"

# 3. Chama Claude API
response = ai_helper.chat(user_input, context)

# 4. Claude retorna resposta educativa
# "Um loop permite repetir código! Existem dois tipos..."

# 5. Resposta é exibida ao usuário
```

### Modelos de Resposta

- **get_hint()**: Dica curta sem spoilers
- **get_explanation()**: Explicação detalhada
- **debug_code()**: Ajuda a encontrar erro
- **chat()**: Conversa livre educativa
- **generate_challenge()**: Desafio personalizado

## Code Executor (Segurança)

### Whitelist de Funções Permitidas

```python
ALLOWED_BUILTINS = {
    'print', 'len', 'range', 'int', 'float', 'str',
    'list', 'dict', 'tuple', 'set', 'bool',
    'abs', 'round', 'sum', 'max', 'min', 'sorted',
    # ... 30+ funções seguras
}
```

### Módulos Permitidos

- `math` - Operações matemáticas
- `random` - Números aleatórios
- `datetime` - Data e hora
- `json` - Serialização

### Sandbox de Robótica

```python
ROBOTICS_NAMESPACE = {
    'LED_VERMELHO': 1,
    'LED_AMARELO': 2,
    'LED_VERDE': 3,
    'MOTOR_ESQUERDO': 4,
    'MOTOR_DIREITO': 5,
    'SENSOR_DISTANCIA': {'valor': 50},
    'ligar_led': lambda pin: ...,
    'motor_frente': lambda pin, vel: ...,
    # ... simulação de robô
}
```

## Deploy Streamlit Cloud

### Fluxo de Deploy

```
GitHub (código)
    │
    └──→ Streamlit Cloud
         │
         ├── Pull código
         ├── Instala dependencies (requirements.txt)
         ├── Executa app.py
         └── Disponibiliza em URL pública
```

### Variáveis de Ambiente

```
ANTHROPIC_API_KEY = sua_chave_segura
```

Armazenadas em "Secrets" do Streamlit Cloud (criptografado)

## Performance

### Otimizações

- **Caching**: Streamlit cache para queries
- **Lazy Loading**: Aulas carregadas sob demanda
- **Timeout**: Limite de 10s para execução de código
- **Histórico**: Último chat mantido em session state

### Métricas

- Tempo de carregamento: <1s
- Execução de código: <2s
- Chat com IA: <5s (depende da API)
- Banco de dados: <100ms por query

## Escalabilidade Futura

### Melhorias Planejadas

1. **Real-time Updates**: WebSockets para chat
2. **Leaderboard**: Ranking de usuários
3. **Multiplayer**: Desafios colaborativos
4. **Mobile App**: React Native
5. **Hardware Integration**: Arduino/Raspberry Pi real
6. **Analytics**: Dashboard para educadores
7. **Certificados**: Emissão automática
8. **Community**: Fórum e showcase

## Testing

### Como Testar Localmente

```bash
# Executar app
streamlit run app.py

# Em outro terminal, testar módulos
python -c "from modules.code_executor import CodeExecutor; \
    result = CodeExecutor.execute('print(\"test\")'); \
    print(result)"
```

### Casos de Teste

- ✅ Execução de código Python básico
- ✅ Validação de código perigoso
- ✅ Cálculo de níveis
- ✅ Adição de pontos
- ✅ Criação de conquistas
- ✅ Chat com IA

## Contribuindo

### Adicionar Nova Aula

1. Edite `config/lessons.py`
2. Adicione em `LESSONS[nivel]['lessons']`
3. Inclua: title, description, content, challenge, robotics
4. Test local: `streamlit run app.py`
5. Commit e push

### Adicionar Novo Desafio

1. Edite `config/challenges.py`
2. Adicione em `EXTRA_CHALLENGES[nivel]`
3. Inclua: title, difficulty, description, expected_output, bonus
4. Commit e push

### Reportar Bug

Abra issue no GitHub com:
- Descrição do problema
- Passos para reproduzir
- Screenshots (se aplicável)
- Seu sistema operacional e versão Python

---

**Versão**: 1.0.0
**Última atualização**: Janeiro 2024
**Mantido por**: CodeMaster Team
