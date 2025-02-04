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

@app.route('/control/<username>')
def control(username):
    return render_template('control.html', username=username)

@app.route('/control', methods=['POST'])
def control_robot():
    username = request.json.get("username")
    x = request.json.get("x")
    y = request.json.get("y")
    if username in clients:
        command = json.dumps({"x": x, "y": y})
        clients[username].send(command.encode())
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Client not found"})

def server_listen():
    server_ip = "0.0.0.0"
    port = 6026
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_ip, port))
    s.listen(5)
    print("Server listening on port 6026")
    
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    threading.Thread(target=server_listen).start()
    app.run(host='0.0.0.0', port=6026)

# HTML Templates

index_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Robot Control</title>
</head>
<body>
    <h1>Connected Robots</h1>
    <ul>
        {% for client in clients %}
        <li><a href="/control/{{ client }}">{{ client }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

control_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Control Robot</title>
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const controlPad = document.getElementById("control-pad");
            const dot = document.getElementById("dot");
            
            function updateDotPosition(x, y) {
                dot.style.left = `${x * 100}%`;
                dot.style.top = `${y * 100}%`;
            }
            
            function sendCoordinates(x, y) {
                fetch('/control', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username: '{{ username }}', x: x, y: y })
                });
            }
            
            function handleMove(event) {
                let rect = controlPad.getBoundingClientRect();
                let x = (event.clientX - rect.left) / rect.width;
                let y = (event.clientY - rect.top) / rect.height;
                x = Math.max(0, Math.min(1, x));
                y = Math.max(0, Math.min(1, y));
                updateDotPosition(x, y);
                sendCoordinates(x, y);
            }
            
            controlPad.addEventListener("mousemove", handleMove);
            controlPad.addEventListener("touchmove", function (event) {
                event.preventDefault();
                handleMove(event.touches[0]);
            });
        });
    </script>
    <style>
        #control-pad {
            width: 200px;
            height: 200px;
            background-color: lightgray;
            border-radius: 50%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        #dot {
            width: 20px;
            height: 20px;
            background-color: red;
            border-radius: 50%;
            position: absolute;
            transform: translate(-50%, -50%);
        }
    </style>
</head>
<body>
    <h1>Controlling {{ username }}</h1>
    <div id="control-pad">
        <div id="dot"></div>
    </div>
</body>
</html>
"""

with open("templates/index.html", "w") as f:
    f.write(index_html)

with open("templates/control.html", "w") as f:
    f.write(control_html)
