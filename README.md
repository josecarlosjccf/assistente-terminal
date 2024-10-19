# Assistente Virtual no Terminal

Este projeto é um assistente virtual simples que usa o modelo `llama3-8b-8192` da Groq para gerar respostas em Português. O chatbot é projetado para rodar no terminal.

## Pré-requisitos

- Python 3.7 ou superior
- Uma chave de API da Groq (cada usuário deve obter sua própria chave)

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/josecarlosjccf/assistente-terminal.git
    cd assistente-terminal
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Obtenha sua chave de API da Groq e crie um arquivo `.env` na raiz do projeto:
    ```plaintext
    GROQ_API_KEY=sua-chave-de-api-aqui
    ```

## Uso

1. Execute o script `chat-bot.py`:
    ```bash
    python chat-bot.py
    ```

2. Interaja com o assistente no terminal:
    ```plaintext
    Você: Olá, como você está?
    Assistente: Estou bem, obrigado! Como posso ajudar hoje?
    ```

3. Digite 'sair' para encerrar a sessão.

## Estrutura do Código

O código principal está no arquivo `chat-bot.py` e segue uma abordagem orientada a objetos com a classe `ChatBot`. Esta classe gerencia a configuração do modelo e a interação com o usuário.

