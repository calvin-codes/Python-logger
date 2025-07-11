from flask import Flask, request, render_template_string
from paths import LOG_PATH

app = Flask(__name__)

@app.route('/')
def show_log():
    selected = request.args.get('level', '')

    try:
        with open(LOG_PATH, 'r') as f:
            all_lines = f.read().splitlines()
            all_lines.reverse()
    except FileNotFoundError:
        all_lines = ["❌ No logs found."]

    return render_template_string(HTML, logs=all_lines, filter=selected)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Live Log Viewer</title>
    <style>
        body {
            font-family: monospace;
            background: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #007acc;
        }
        .log-line {
            font-size: 0.95em;
            }
        .error    { color: #d8000c; background: #ffd2d2; font-weight: bold; }
        .warning  { color: #9f6000; }
        .info     { color: #00529b; }
        .debug    { color: #666666; }
    </style>
</head>
<body>
    <h1>📜 Live Log – project.log</h1>
    <form method="get">
        <label for="level">Filter:</label>
        <select name="level" id="level">
            <option value="">Alle</option>
            <option value="ERROR">ERROR</option>
            <option value="WARNING">WARNING</option>
            <option value="INFO">INFO</option>
            <option value="DEBUG">DEBUG</option>
        </select>
        <button type="submit">Filter</button>
    </form>
    <pre>
{% for line in logs %}
    {% if not filter or filter in line %}
        {% if 'ERROR' in line %}
            <div class="log-line error">{{ line }}</div>
        {% elif 'WARNING' in line %}
            <div class="log-line warning">{{ line }}</div>
        {% elif 'INFO' in line %}
            <div class="log-line info">{{ line }}</div>
        {% elif 'DEBUG' in line %}
            <div class="log-line debug">{{ line }}</div>
        {% else %}
            <div class="log-line">{{ line }}</div>
        {% endif %}
    {% endif %}
{% endfor %}
    </pre>
    <script>
window.scrollTo(0, 0);
</script>

</body>
</html>
"""


if __name__ == '__main__':
    app.run()
