from flask import Flask, render_template
from flask_jsonrpc import JSONRPC
from flask_socketio import SocketIO
import requests
import mongoengine


app = Flask(__name__, static_folder='/home/bodhi/PycharmProjects/chat_pulsepro/')
app.config['SECRET_KEY'] = 'my_key'

if __name__ == '__main__':
    jsonrpc = JSONRPC(app, '/api')
    socketio = SocketIO(app)


@app.route('/')
def chat_room():
    return render_template('chat_room.html')


@socketio.on('my event')
def handle_message(json, methods=['GET', 'POST']):
    user_name_info = requests.form['user_name']
    message_info = requests.form['message']
    add_info = Dialogue(user=user_name_info, message=message_info)
    add_info.save()
