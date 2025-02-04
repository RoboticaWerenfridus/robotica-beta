import socket
import json
import threading
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

clients = {}

def handle_client(conn, addr):
    data = conn.recv(1024).decode()
    credentials = json.loads(data)
    username = credentials.get("username")
    password = credentials.get("password")
    
    if username and password:
        clients[username] = conn
        conn.send("Authenticated".encode())
        print(f"{username} connected from {addr}")
        
        while True:
            try:
                command = conn.recv(1024).decode()
                if not command:
                    break
                print(f"Command received from {username}: {command}")
            except:
                break
        
    del clients[username]
    conn.close()

@app.route('/')
def index():
    return render_template('index.html', clients=clients.keys())

@app.route('/control', methods=['POST'])
def control_robot():
    username = request.json.get("username")
    command = request.json.get("command")
    if username in clients:
        clients[username].send(command.encode())
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Client not found"})

def server_listen():
    server_ip = "0.0.0.0"
    port = 6026
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_ip, port))
    s.listen(5)
    print("Server listening on port 5000")
    
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    threading.Thread(target=server_listen).start()
    app.run(host='0.0.0.0', port=6026)
