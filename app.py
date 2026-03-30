
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Download File</title>

<style>
body{
    font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    background:#f2f2f7;
    display:flex;
    height:100vh;
    align-items:center;
    justify-content:center;
}

button{
    padding:15px 25px;
    font-size:18px;
    border:none;
    border-radius:12px;
    background:#007aff;
    color:white;
    cursor:pointer;
}
</style>

</head>

<body>

<a href="/download">
<button>Download Project</button>
</a>

</body>
</html>
"""

@app.route("/download")
def download():
    return send_file("correct1.py.zip", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True). 