from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Active WebSockets avec CORS
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def index():
    return "Serveur Flask avec SocketIO"


@socketio.on("message")
def handle_message(msg):
    print(f"Message reçu: {msg}")
    if request.args.get("username") == "claire":
        emit("response", "hello claire")
    else:
        emit(
            "response", "Help! unauthorized user", broadcast=True
        )  # Répond à tous les clients


@socketio.on("connect")
def handle_connect():
    # user_name = request.args.get("username")
    # print(f"Client connecté: {user_name} avec le sid {request.sid}")
    emit("response", "Bienvenue sur le serveur WebSocket!")


@socketio.on("disconnect")
def handle_disconnect():
    print(f"Client déconnecté: {request.sid}")


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
