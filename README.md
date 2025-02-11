# Criando sua própria IA

Para criarmos a nossa IA sem a necessidade de Internet

# Vídeo

[![Video_Ollama](https://img.youtube.com/vi/hDZb18TAxjc/0.jpg)](https://www.youtube.com/watch?v=hDZb18TAxjc) 


# Instalação
```
sudo systemctl start docker
docker pull ollama/ollama:latest
docker run -d --name ollama -p 11434:11434 ollama/ollama  # Reinicia
```

# Executa o modelo
```
 ollama run cybersoul
```

# Instalando o Chainlit Chat
```
pip install chainlit
chainlit chat
```

# Criando tradução para Português
https://docs.chainlit.io/customisation/translation

# Portas
- 11434: Ollama

# Dependências
- [Chainlit](https://chainlit.io/)
- [Ollama](https://ollama.com/)

