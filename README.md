
# 🧾 Documentação Técnica — Chat FURIA

## 📌 Visão Geral

**Chat FURIA** é uma aplicação web de chat em tempo real com um bot que responde a comandos relacionados ao time de CS:GO da FURIA. A aplicação é construída com **Flask** e **Flask-SocketIO**, e serve como uma experiência conversacional voltada para fãs da organização.

## 🧱 Arquitetura

A aplicação segue uma arquitetura básica:

- `Flask` como servidor HTTP principal
- `Flask-SocketIO` para comunicação em tempo real (WebSockets)
- `HTML + CSS + JavaScript` no front-end
- Um módulo separado (`data.py`) para tratar os dados de resposta do bot

## 📁 Estrutura de Diretórios

```
chat-furia/
├── app.py                # App Flask principal
├── data.py               # Funções que retornam dados do bot
├── requirements.txt      # Dependências do projeto
│
├── templates/
│   └── index.html        # Interface HTML do chat
│
├── static/
│   ├── style.css         # Estilo visual
│   └── script.js         # Lógica JS do Socket.IO
```

## 🚀 Instalação e Execução

### 1. Requisitos

- Python 3.8+
- pip

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
python app.py
```

### 4. Acesse via navegador

```
http://localhost:5000
```

## 💡 Funcionalidades

### Chat em Tempo Real

Usuários podem se comunicar em tempo real digitando seu nome e mensagem. As mensagens são transmitidas via `WebSocket` usando `Flask-SocketIO`.

### Bot Interativo

O bot responde automaticamente aos seguintes comandos prefixados com `/`:

| Comando     | Descrição                                |
|-------------|--------------------------------------------|
| `/agenda`   | Exibe os próximos jogos da FURIA          |
| `/elenco`   | Mostra o elenco atual                     |
| `/noticias` | Traz notícias recentes sobre o time       |
| `/redes`    | Exibe os links das redes sociais oficiais |
| `/loja`     | Lista alguns produtos da loja oficial     |

## ⚙️ Explicação Técnica dos Arquivos

### `app.py`

- Define as rotas com Flask
- Inicializa `SocketIO`
- Escuta eventos de conexão (`connect`) e mensagem (`message`)
- Encaminha os comandos para funções específicas do `data.py`
- Emite mensagens formatadas para o front-end

### `data.py`

Contém funções que retornam strings com as respostas do bot.

### `index.html`

HTML simples contendo:

- Campo de nome
- Campo de mensagem
- Container para exibir mensagens

### `script.js`

- Captura o envio da mensagem com `Enter`
- Usa `Socket.IO` para enviar/receber mensagens
- Exibe as mensagens dinamicamente no chat

### `style.css`

Estilo visual escuro com destaque em amarelo (referência à identidade da FURIA).

## 🔧 APIs de Comando

Não há APIs REST nesta aplicação, já que a comunicação é feita via WebSockets. Os eventos principais são:

### `connect`

Evento chamado ao conectar. Retorna mensagem de boas-vindas com lista de comandos.

### `message`

Envia uma mensagem ao servidor. Se começar com `/`, o servidor interpreta como comando do bot.

## 📦 Dependências

```txt
flask
flask-socketio
```

## 📄 Possíveis Extensões Futuras

- Integração com API real da FURIA (para agenda ou notícias)
- Autenticação de usuários
- Suporte a emojis ou imagens
- Banco de dados para histórico de mensagens

## 🙋 Suporte e Contribuição

Para contribuir:

1. Fork este repositório
2. Crie uma branch com sua feature: `git checkout -b nova-feature`
3. Faça commit: `git commit -m "feat: adiciona nova feature"`
4. Push para o branch remoto: `git push origin nova-feature`
5. Abra um Pull Request
