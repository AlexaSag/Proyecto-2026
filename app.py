from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Alexa Builder</title>
</head>

<body>

<h1>Alexa Builder</h1>

<!--
VERSION ANTERIOR DEL PROYECTO

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "test"

FIN DE NOTA
-->

<a href="/download">
<button>Download Project</button>
</a>

</body>
</html>
"""

@app.route("/download")
def download():
    return send_file("s.a.brain.py.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)