# Criando sua própria IA

Para criarmos a nossa IA sem a necessidade de Internet

# Vídeo

[![Vídeo Criando sua IA sem independência de internet](https://youtu.be/hDZb18TAxjc)]


# Instalação
```
sudo systemctl start docker
pkill ollama  # Mata processos antigos
docker pull ollama/ollama:latest
docker stop ollama && docker rm ollama  # Remove o container antigo
docker run -d --name ollama -p 11434:11434 ollama/ollama  # Reinicia
```
# Criando seu próprio modelo
Para criar o seu próprio modelo você deve criar um arquivo **Modelfile** sem extensão,
é aqui neste arquivo que você irá definir alguns comportamentos na sua LLM

Por exemplo, você pode definir um nome para ela e também que ela saiba um pouco sobre você

# Comandos para gerar seu modelo
```
# Remove o modelo
 ollama rm cybersoul

# Cria o modelo 
 ollama create cybersoul -f ./Modelfile

# Executa o modelo
 ollama run cybersoul
```

# Instalando o Chainlit Chat
```
pip install chainlit
chainlit chat
```

# Portas
- 11434: Ollama

# Dependências
- [Chainlit](https://chainlit.io/)
- [Ollama](https://ollama.com/)

