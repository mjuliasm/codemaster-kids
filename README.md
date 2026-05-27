# 🚀 CodeMaster Kids - Plataforma de Aprendizado de Programação

Uma plataforma gamificada e interativa para ensinar **programação profissional** a crianças de 11 anos, integrando **Python, SQL, IA** e **robótica**.

## 🎯 Objetivos da Plataforma

✅ Ensinar programação REAL (não blocos visuais)  
✅ Integrar conceitos de robótica com exemplos práticos  
✅ Gamificação com sistema de níveis e recompensas  
✅ Uso de IA como ferramenta educacional  
✅ Progressão estruturada: Python → SQL → IA  
✅ Projetos práticos e desafios hands-on  

## 📋 Estrutura do Curso

### 🟢 **Nível 1: Fundamentos Python (Semanas 1-3)**
- Variáveis, tipos de dados
- Estruturas de controle (if, for, while)
- Funções básicas
- **Robótica**: Controle de LEDs e motores

### 🟡 **Nível 2: Python Intermediário (Semanas 4-6)**
- Listas, dicionários, tuplas
- Manipulação de strings
- Tratamento de erros
- **Robótica**: Sensores e lógica condicional

### 🟠 **Nível 3: Estrutura de Dados & Algoritmos (Semanas 7-9)**
- Ordenação e busca
- Complexidade de algoritmos
- Recursão
- **Robótica**: Algoritmos de navegação

### 🔴 **Nível 4: Banco de Dados com SQL (Semanas 10-12)**
- SELECT, INSERT, UPDATE, DELETE
- JOINs e queries complexas
- Design de banco de dados
- **Robótica**: Armazenamento de dados de sensores

### 🟣 **Nível 5: IA e Machine Learning (Semanas 13-15)**
- Introdução a IA
- Datasets e treinamento
- Modelos simples de previsão
- **Robótica**: IA em robôs autônomos

## 🛠️ Stack Técnico

- **Frontend**: Streamlit (Python)
- **Backend**: Python puro
- **Banco de Dados**: SQLite
- **IA**: Integração com Claude API
- **Deployment**: Streamlit Cloud

## 🚀 Como Começar

### Localmente
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/codemaster-kids.git
cd codemaster-kids

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
echo "ANTHROPIC_API_KEY=sua_chave_aqui" > .env

# Execute a aplicação
streamlit run app.py
```

### Deploy no Streamlit Cloud
1. Faça push do código para seu repositório GitHub
2. Acesse [streamlit.io/cloud](https://share.streamlit.io/)
3. Conecte seu repositório GitHub
4. Configure a variável de ambiente `ANTHROPIC_API_KEY` nos secrets
5. Deploy automático!

## 📁 Estrutura do Repositório

```
codemaster-kids/
├── app.py                    # Aplicação principal Streamlit
├── config/
│   ├── levels.json          # Configuração dos níveis
│   ├── challenges.json      # Desafios e exercícios
│   └── achievements.json    # Sistema de achievements
├── modules/
│   ├── auth.py             # Autenticação simples
│   ├── gamification.py      # Sistema de gamificação
│   ├── code_executor.py     # Executor de código seguro
│   ├── ai_helper.py         # Integração com IA Claude
│   └── database.py          # Gerenciamento de dados
├── lessons/
│   ├── level1_python/      # Aulas Nível 1
│   ├── level2_python/      # Aulas Nível 2
│   ├── level3_algorithms/  # Aulas Nível 3
│   ├── level4_sql/         # Aulas Nível 4
│   └── level5_ai/          # Aulas Nível 5
├── requirements.txt
├── .env.example
└── README.md
```

## 📚 Funcionalidades Principais

### 1. **Sistema de Gamificação**
- 🏆 Pontos por desafios completados
- 🎖️ Badges e achievements
- 📈 Sistema de níveis progressivo
- 🔥 Streak diário
- 🎁 Recompensas desbloqueáveis

### 2. **Editor de Código Integrado**
- Syntax highlighting
- Execução segura de código
- Feedback em tempo real
- Dicas inteligentes com IA

### 3. **Lições Interativas**
- Conteúdo estruturado por nível
- Exemplos práticos
- Desafios progressivos
- Integração com robótica

### 4. **Sistema de Robótica**
- Simulação de circuitos
- Controle de componentes
- Integração com código Python
- Exemplos do mundo real

### 5. **Assistente de IA**
- Respostas personalizadas
- Dicas sem spoilers
- Explicações em linguagem simples
- Sugestões de próximos passos

## 🎮 Como Usar

1. **Criar Conta**: Cadastro simples com nome e idade
2. **Escolher Nível**: Começar no Nível 1
3. **Aprender**: Ler lição e entender conceitos
4. **Desafiar**: Resolver exercícios práticos
5. **Praticar**: Fazer projetos integradores
6. **Progredir**: Ganhar pontos e desbloquear próximo nível

## 🔐 Segurança

- Execução de código em sandbox
- Sem acesso a arquivos do sistema
- Limite de tempo de execução
- Variáveis de ambiente protegidas

## 📈 Roadmap

- [ ] Multiplicador de pontos por streak
- [ ] Sistema de leaderboard
- [ ] Desafios colaborativos
- [ ] Integração com Arduino real
- [ ] App mobile
- [ ] Certificados ao completar níveis
- [ ] Comunidade de alunos

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:
1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💼 Autor

Criado com ❤️ para ensinar crianças a programar de verdade.

## 📧 Contato

Dúvidas? Abra uma issue no repositório!

---

**Comece agora**: [Acesse a plataforma ao vivo](https://seu-app.streamlit.app)
