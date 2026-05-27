# 🚀 INSTALAÇÃO RÁPIDA - CodeMaster Kids

## 5 MINUTOS PARA RODAR LOCALMENTE

### Pré-requisitos
- Python 3.8+
- Git
- Chave de API Anthropic (gratuita em https://console.anthropic.com)

### Passos

```bash
# 1. Clonar repositório
git clone https://github.com/seu-usuario/codemaster-kids.git
cd codemaster-kids

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar API key
cp .env.example .env
# Edite .env e adicione sua chave Anthropic

# 5. Executar aplicação
streamlit run app.py
```

### URL Local
Abra seu navegador: **http://localhost:8501**

---

## DEPLOY NO STREAMLIT CLOUD (10 MINUTOS)

### Pré-requisitos
- Repositório GitHub com o código
- Conta Streamlit Cloud (gratuita)
- Chave Anthropic API

### Passos

1. **Push para GitHub**
```bash
git add .
git commit -m "Deploy CodeMaster Kids"
git push origin main
```

2. **Acessar Streamlit Cloud**
- Vá para https://share.streamlit.io/
- Clique "New app"

3. **Configurar aplicação**
- Repository: `seu-usuario/codemaster-kids`
- Branch: `main`
- Main file path: `app.py`
- Click "Deploy"

4. **Adicionar Secret (API Key)**
- Após deploy, clique em "Manage app"
- Vá para "Secrets"
- Adicione: `ANTHROPIC_API_KEY=sua_chave_aqui`
- Salve

5. **Pronto!**
Seu app estará em: `https://seu-app-name.streamlit.app`

---

## TROUBLESHOOTING

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### "ANTHROPIC_API_KEY not found"
1. Certifique-se de ter `.env` criado
2. API key correta (começa com `sk-`)
3. Reinicie o streamlit: `Ctrl+C` e `streamlit run app.py`

### "Port 8501 already in use"
```bash
streamlit run app.py --server.port 8502
```

### App não carrega após deploy
- Aguarde 2-3 minutos
- Verifique logs em Streamlit Cloud
- Confirm que secret foi adicionado corretamente

---

## PRÓXIMOS PASSOS

✅ **Local**: Acesse http://localhost:8501
✅ **Cloud**: Acesse sua URL do Streamlit
✅ **Criar Conta**: Use qualquer username
✅ **Começar**: Inicie o Nível 1!

---

**Documentação Completa**: Veja `README.md` para mais detalhes
