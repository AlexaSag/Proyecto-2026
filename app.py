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

<h1>Alexa Builder</h1>

<!--
NO LONGER FILE. POR FAVOR DE CONTACTARSE CON A.S.

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