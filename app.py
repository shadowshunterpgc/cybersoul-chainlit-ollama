import json
import chainlit as cl
import requests
import os

# Configurar a URL do Ollama
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_URL = f"{OLLAMA_HOST}/api/generate"


def ask_ollama(prompt):
    """Envia um prompt para o Ollama e processa a resposta em streaming"""
    try:
        data = {"model": "llama3.2", "prompt": prompt, "stream": True}  # Ativar streaming
        with requests.post(OLLAMA_URL, json=data, stream=True, timeout=10) as response:
            response.raise_for_status()

            collected_response = ""  # String para armazenar a resposta completa

            for line in response.iter_lines():
                if line:
                    json_line = line.decode('utf-8')  # Decodificar a linha
                    try:
                        json_data = json.loads(json_line)  # Converter para JSON
                        collected_response += json_data.get("response", "")  # Concatenar resposta
                    except requests.exceptions.JSONDecodeError:
                        continue  # Ignorar erros de JSON mal formado

            return collected_response if collected_response else "Erro ao processar resposta do modelo."

    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar com o Ollama: {e}"


@cl.on_chat_start
async def start():
    """Mensagem de boas-vindas quando o chat inicia"""
    await cl.Message(content="Bem-vindo! Você está conectado a Cybersoul.").send()


@cl.on_message
async def main(message):
    """Recebe as mensagens do usuário e envia para o Ollama"""
    response = ask_ollama(message.content)
    await cl.Message(content=response).send()
