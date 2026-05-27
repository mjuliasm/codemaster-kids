# 📚 Guia de Deploy - CodeMaster Kids

## Pré-requisitos

1. **Conta no GitHub** - Para hospedar o código
2. **Conta Anthropic** - Para usar Claude API
3. **Conta Streamlit Cloud** - Para deploy da aplicação

## Passo 1: Preparar o Repositório GitHub

```bash
# Clonar ou criar novo repositório
git clone https://github.com/seu-usuario/codemaster-kids.git
cd codemaster-kids

# Inicializar git (se novo)
git init

# Criar arquivo .gitignore
echo "
.env
__pycache__/
*.pyc
.pytest_cache/
.streamlit/secrets.toml
data/
venv/
*.db
" > .gitignore

# Adicionar todos os arquivos
git add .
git commit -m "Initial commit: CodeMaster Kids - Plataforma de Aprendizado"
git push origin main
```

## Passo 2: Configurar Chave da API Anthropic

1. Acesse [console.anthropic.com](https://console.anthropic.com)
2. Crie uma nova chave de API
3. Copie a chave (você precisará dela no passo 5)

## Passo 3: Deploy no Streamlit Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io/)
2. Clique em "New app"
3. Preencha:
   - **Repository**: seu-usuario/codemaster-kids
   - **Branch**: main
   - **Main file path**: app.py
4. Clique em "Deploy"

## Passo 4: Configurar Secrets

1. Na página do seu app no Streamlit Cloud
2. Clique em "Rerun" (engrenagem) → "Manage app"
3. Vá para "Secrets"
4. Cole este conteúdo:

```
ANTHROPIC_API_KEY=sua_chave_aqui
```

5. Clique em "Save"
6. O app será refeito automaticamente

## Passo 5: Verificar o Deploy

1. Acesse a URL fornecida pelo Streamlit
2. Crie uma nova conta
3. Comece com a primeira aula!

## 🎯 Seu app estará disponível em:
`https://seu-app-name.streamlit.app`

## Troubleshooting

### Erro de API Key
- Certifique-se de que a chave está correta em Secrets
- Copie novamente da console Anthropic

### App não aparece
- Aguarde 2-3 minutos para o deploy completar
- Atualize a página do navegador

### Erro de módulos
- Verifique se `requirements.txt` está na raiz
- Todos os imports estão corretos

## Atualizando o App

Após fazer mudanças no código:

```bash
git add .
git commit -m "Descrição das mudanças"
git push origin main
```

O Streamlit Cloud detectará as mudanças e refará o app automaticamente!

## Customizações

### Adicionar mais lições
- Edite `config/lessons.py`
- Adicione novos níveis e aulas
- Push para GitHub

### Modificar gamificação
- Edite `modules/gamification.py`
- Altere pontos, badges, níveis
- Push para GitHub

### Melhorar o design
- Edite o CSS em `app.py`
- Adicione novas cores e estilos
- Push para GitHub

---

**Parabéns! Seu app educativo está no ar!** 🚀
