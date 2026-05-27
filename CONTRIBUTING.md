# 🤝 Guia de Contribuição - CodeMaster Kids

Obrigado por querer contribuir para CodeMaster Kids! Este documento ajudará você a entender como contribuir.

## 📋 Código de Conduta

- ✅ Seja respeitoso com todos
- ✅ Focado em aprender e ensinar
- ✅ Crítica construtiva
- ✅ Celebre as vitórias dos outros
- ❌ Nenhuma discriminação
- ❌ Spam ou auto-promoção

## 🚀 Como Contribuir

### 1. **Reportar um Bug**

Se encontrou um problema, abra uma issue com:

```
Título: [BUG] Descrição breve do problema

Descrição:
- O que você esperava?
- O que aconteceu?
- Quando ocorre?

Passos para reproduzir:
1. ...
2. ...
3. ...

Informações do sistema:
- OS: [Windows/Mac/Linux]
- Python: [versão]
- Navegador: [se relevante]

Screenshots: [se aplicável]
```

### 2. **Sugerir uma Melhoria**

Abra uma issue com:

```
Título: [FEATURE] Descrição da melhoria

Descrição:
- Por que precisamos disso?
- Como deveria funcionar?
- Exemplos de uso

Benefícios:
- Melhora aprendizado
- Mais engajamento
- ...
```

### 3. **Enviar um Pull Request**

#### Configurar seu ambiente

```bash
# 1. Fork o repositório no GitHub

# 2. Clone seu fork
git clone https://github.com/seu-usuario/codemaster-kids.git
cd codemaster-kids

# 3. Crie uma branch
git checkout -b feature/sua-feature

# 4. Instale dependências
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 5. Faça suas mudanças
# Edite os arquivos necessários

# 6. Teste localmente
streamlit run app.py

# 7. Commit suas mudanças
git add .
git commit -m "Descrição clara das mudanças"

# 8. Push para sua branch
git push origin feature/sua-feature

# 9. Abra um Pull Request no GitHub
```

#### Critérios de qualidade

- ✅ Código limpo e bem comentado
- ✅ Segue o style do projeto
- ✅ Testado localmente
- ✅ Documentação atualizada
- ✅ Mensagem de commit clara

## 📝 Tipos de Contribuição

### Adicionar Novas Aulas

**Arquivo**: `config/lessons.py`

```python
{
    "id": 6,
    "title": "Sua Nova Aula",
    "description": "O que o aluno vai aprender",
    "content": """
# Título em Markdown

## Conceito
Explicação clara do conceito

## Exemplo
```python
# Código de exemplo
```

## Desafio
    """,
    "challenge": "Descrição do desafio",
    "robotics": "Como isso se aplica em robótica"
}
```

### Adicionar Novos Desafios

**Arquivo**: `config/challenges.py`

```python
{
    "id": 3,
    "title": "Nome do Desafio",
    "difficulty": "Fácil/Médio/Difícil",
    "description": "Descrição clara",
    "expected_output": "O que esperar",
    "bonus": "Desafio extra opcional"
}
```

### Melhorar o Assistente de IA

**Arquivo**: `modules/ai_helper.py`

```python
def nova_funcionalidade(self, parametro):
    """
    Descrição clara
    
    Args:
        parametro: descrição
    
    Returns:
        resultado esperado
    """
    # Sua implementação
```

### Melhorar a Interface

**Arquivo**: `app.py`

- CSS em `st.markdown()`
- Componentes Streamlit
- Responsividade
- Acessibilidade

## 🎨 Guia de Estilo

### Python

```python
# Imports organizados
import os
from datetime import datetime
import streamlit as st

# Nomes descritivos
def calculate_user_level(total_points):
    """Docstring clara"""
    pass

# Comentários quando necessário
# TODO: Implementar feature X
# BUG: Corrigir issue Y
```

### Nomenclatura

- Classes: `PascalCase` - `UserAuth`
- Funções: `snake_case` - `get_user_info`
- Constantes: `UPPER_CASE` - `MAX_TIMEOUT`
- Variáveis: `snake_case` - `user_points`

## 🧪 Testando Mudanças

```bash
# Teste o código localmente
streamlit run app.py

# Verifique se todos os imports funcionam
python -c "from modules.auth import UserAuth; print('OK')"

# Teste a funcionalidade novo
# - Crie conta
# - Faça aula
# - Execute código
# - Use IA
```

## 📚 Documentação

Se sua contribuição muda o comportamento:

- Atualize `README.md` se necessário
- Documente em `GUIDE.md` se for feature
- Atualize `ARCHITECTURE.md` se for estrutural
- Adicione docstrings em Python

## 🐛 Bugs Conhecidos

Veja [Issues no GitHub](https://github.com/seu-usuario/codemaster-kids/issues)

## ❓ Dúvidas?

- Abra uma issue em "Discussions"
- Mencione @seu-usuario
- Seja específico na pergunta

## 🎓 Primeiros Passos

### Para Iniciantes

1. Veja issues com label `good-first-issue`
2. Comece com algo pequeno
3. Pergunte no PR se tiver dúvidas
4. Aprenda com o feedback

### Ideias Fáceis para Começar

- [ ] Adicionar nova aula
- [ ] Adicionar novo desafio
- [ ] Melhorar documentação
- [ ] Corrigir typos
- [ ] Melhorar CSS
- [ ] Adicionar comentários
- [ ] Criar função helper
- [ ] Adicionar validação

## ✨ Reconhecimento

Colaboradores são listados em:
- `CONTRIBUTORS.md` (em breve)
- GitHub contributors page
- Readme do projeto

## 📋 Processo de Review

1. Sua PR é revisada
2. Feedback é fornecido
3. Você faz as mudanças solicitadas
4. PR é aprovada
5. Merge no `main`
6. Deploy automático em produção

## 🔄 Mantendo Seu Fork Atualizado

```bash
# Adicionar upstream
git remote add upstream https://github.com/original/codemaster-kids.git

# Atualizar
git fetch upstream
git rebase upstream/main
git push origin main
```

## 📜 Licença

Por contribuir, você concorda que suas contribuições
serão lincenciadas sob a MIT License.

---

**Obrigado por contribuir! 🙏**

Seu trabalho ajuda crianças a aprender programação de verdade! 🚀
