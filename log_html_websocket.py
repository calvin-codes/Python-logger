#run: python3 /Users/calvin/Documents/SQL_Portfolio/log_viewer_websocket.py

from flask import Flask, render_template_string, request
from flask_socketio import SocketIO
import time
from paths import LOG_PATH

app = Flask(__name__)
socketio = SocketIO(app,
                    cors_allowed_origins="*",
                    async_mode="threading")

@socketio.on('connect')
def on_connect():
    print("✅ Client connected")

HTML = """
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Live Log Viewer</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: "Segoe UI", sans-serif;
      background-color: #f9f9f9;
      color: #333;
    }

    header {
      background-color: #ffffff;
      border-bottom: 1px solid #ddd;
      padding: 1rem 2rem;
      font-size: 1.5rem;
      font-weight: 600;
      text-align: center;
      color: #444;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
    }

    #log {
      margin: 2rem;
      font-size: 1rem;
    }

    .log-line.info   { color: #2d7dd2; }
    .log-line.error  { color: #d93838; font-weight: bold; }
    .log-line.warn   { color: #f4a261; }
    .log-line.system { color: gray; font-style: italic; }

    .status {
      text-align: center;
     font-size: 0.95rem;
     color: gray;
     margin-bottom: 1rem;
    }
  </style>
</head>
<body>
  <header>📡 Live Log Viewer</header>
  <div id="status" class="status"></div>
  <button id="stopBtn">🛑 Stop Log-Monitor</button>
  <div id="log"></div>

  <script src="https://cdn.socket.io/4.6.1/socket.io.min.js"></script>
  <script>
    const socket = io();

    socket.on("disconnect", () => {
      console.log("🔴 WebSocket disconnected");
      const status = document.getElementById("status");
      status.innerText = "🔴 Offline";
    });
    
    socket.on("connect", () => {
      console.log("🟢 connected with server");
      document.getElementById("status").innerText = "🟢 Online";
    });

    socket.on("log_update", function(data) {
      console.log("📨 recieved:", data);
      const logArea = document.getElementById("log");

      let cssClass = "info";
      const text = data.toLowerCase();
      if (text.includes("error") || text.includes("fehler")) cssClass = "error";
      else if (text.includes("warn") || text.includes("achtung")) cssClass = "warn";
      else if (text.includes("client") || text.includes("verbindung")) cssClass = "system";

      const line = `<span class="log-line ${cssClass}">${data}</span><br>`;
      logArea.innerHTML = line + logArea.innerHTML;
    });
    document.getElementById("stopBtn").addEventListener("click", () => {
      socket.emit("stop_monitor");
    });
  </script>
</body>
</html>
"""



@app.route('/')
def index():
    return render_template_string(HTML)



monitor_active = True

def monitor_log():
    global monitor_active
    monitor_active = True
    try:
        with open(LOG_PATH, 'r', buffering=1) as f:
            f.seek(0, 2)
            while monitor_active:
                line = f.readline()
                if line:
                    msg = line.strip()
                    print("→ send:", msg)
                    socketio.emit('log_update', msg)
                socketio.sleep(0.3)
    except Exception as e:
        print("❌ Error in Log-Monitor:", e)

@socketio.on("stop_monitor")
def stop_log_monitor():
    global monitor_active
    monitor_active = False
    print("⛔ Log-Monitor stopped by browser")
    socketio.emit("log_update", "⛔ Log-Monitor stopped")


if __name__ == '__main__':
    socketio.start_background_task(monitor_log)
    socketio.run(app)
