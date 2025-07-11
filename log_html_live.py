#1. install flask
#2. then run this code in terminal
#3. open host in browser:
#cltr + C to quit this server

from flask import Flask, render_template_string
import time
from paths import LOG_PATH

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Live Log Viewer</title>
    <meta http-equiv="refresh" content="2"> <!-- update every 2 seconds -->
    <style>
        body { font-family: monospace; background: #111; color: #0f0; padding: 1em; }
        h1 { color: #0ff; }
        pre { white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>📜 Live Log – project.log</h1>
    <pre>{{ logs }}</pre>
</body>
</html>
"""

@app.route('/')
def show_log():
    try:
        with open(LOG_PATH, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = "❌ No logs found."
    return render_template_string(HTML, logs=content)

if __name__ == '__main__':
    app.run()
