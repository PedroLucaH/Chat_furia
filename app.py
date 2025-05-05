from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from data import get_elenco, get_agenda, get_noticias, get_redes, get_loja

app = Flask(__name__)
app.config['SECRET_KEY'] = 'furiafan'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    mensagem_boas_vindas = (
        "👋 Bem-vindo ao chat da FURIA!\n"
        "Use os comandos abaixo para interagir com o bot:\n"
        "- /agenda → Ver os próximos jogos\n"
        "- /elenco → Ver o elenco atual\n"
        "- /noticias → Últimas notícias\n"
        "- /redes → Ver redes sociais oficiais\n"
        "- /loja → Ver produtos oficiais da FURIA"
    )
    emit('message', {'user': 'BOT', 'msg': mensagem_boas_vindas})

@socketio.on('message')
def handle_message(data):
    user = data.get('user', 'Anônimo')
    msg = data.get('msg', '').strip()

    if msg.startswith('/'):
        if msg == '/agenda':
            emit('message', {'user': 'BOT', 'msg': get_agenda()})
        elif msg == '/elenco':
            emit('message', {'user': 'BOT', 'msg': get_elenco()})
        elif msg == '/noticias':
            emit('message', {'user': 'BOT', 'msg': get_noticias()})
        elif msg == '/redes':
            emit('message', {'user': 'BOT', 'msg': get_redes()})
        elif msg == '/loja':
            emit('message', {'user': 'BOT', 'msg': get_loja()})
        else:
            emit('message', {'user': 'BOT', 'msg': '❌ Comando não reconhecido.'})
    else:
        emit('message', {'user': user, 'msg': msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
