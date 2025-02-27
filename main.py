from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Active WebSockets avec CORS


@app.route("/")
def index():
    return "Serveur Flask avec SocketIO"


@socketio.on("message")
def handle_message(msg):
    print(f"Message reçu: {msg}")
    emit(
        "response", f"Message reçu: {msg}", broadcast=True
    )  # Répond à tous les clients


@socketio.on("connect")
def handle_connect():
    print(f"Client connecté: {request.sid}")
    emit("response", "Bienvenue sur le serveur WebSocket!")


@socketio.on("disconnect")
def handle_disconnect():
    print(f"Client déconnecté: {request.sid}")


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
