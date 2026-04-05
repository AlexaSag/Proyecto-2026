from flask import Flask

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

<h1>no longer available. contactarse con A.S.</h1>

<!--
VERSION ANTERIOR DEL PROYECTO

from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "test"

FIN DE NOTA
-->

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)