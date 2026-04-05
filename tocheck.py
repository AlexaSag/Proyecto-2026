from http.server import BaseHTTPRequestHandler, HTTPServer

class MiServidor(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.enviar_inicio()
        else:
            self.enviar_404()

    def enviar_inicio(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lumen</title>

<style>

/* 🌌 FONDO SPACE */
body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: radial-gradient(circle at 20% 30%, #1a2338, #0b0f1a 60%);
    color: #F8FAFC;
}

/* ✨ CONTENEDOR */
.container {
    max-width: 900px;
    margin: auto;
    padding: 40px 20px;
}

/* 🌠 LOGO */
.logo {
    text-align: center;
    font-size: 42px;
    letter-spacing: 6px;
    font-weight: 600;
    margin-bottom: 30px;
    background: linear-gradient(90deg, #3B82F6, #22D3EE);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* 🧊 CARD */
.card {
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

/* 🔘 BOTONES */
button {
    padding: 14px 20px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(135deg, #3B82F6, #22D3EE);
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(59,130,246,0.5);
}

/* 📥 INPUT */
input {
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    border: none;
    margin-top: 10px;
    margin-bottom: 15px;
    background: rgba(255,255,255,0.08);
    color: white;
}

/* 📊 RESULTADO */
.result {
    margin-top: 10px;
    color: #22D3EE;
    font-weight: 500;
}

/* ✨ FOOTER */
.footer {
    text-align: center;
    opacity: 0.5;
    margin-top: 30px;
    font-size: 12px;
}

</style>
</head>

<body>

<div class="container">

    <div class="logo">LUMEN</div>

    <!-- 🧮 CALCULADORA -->
    <div class="card">
        <h3>Quick Calculator</h3>
        <input type="number" id="num1" placeholder="Number 1">
        <input type="number" id="num2" placeholder="Number 2">
        <button onclick="calculate()">Calculate</button>
        <div class="result" id="result"></div>
    </div>

    <!-- 📋 TEMPLATE GENERATOR -->
    <div class="card">
        <h3>Template Generator</h3>
        <input type="text" id="name" placeholder="Name">
        <button onclick="generate()">Generate</button>
        <div class="result" id="template"></div>
    </div>

    <!-- 🌐 QUICK LINKS -->
    <div class="card">
        <h3>Quick Tools</h3>
        <button onclick="openGoogle()">Google</button>
        <button onclick="openMaps()">Maps</button>
    </div>

    <div class="footer">Lumen • clarity through efficiency</div>

</div>

<script>

/* 🧮 CALCULADORA */
function calculate(){
    let a = parseFloat(document.getElementById("num1").value);
    let b = parseFloat(document.getElementById("num2").value);
    let result = a + b;
    document.getElementById("result").innerText = "Result: " + result;
}

/* 📋 TEMPLATE */
function generate(){
    let name = document.getElementById("name").value;
    document.getElementById("template").innerText =
    "Hello " + name + ", your request has been processed.";
}

/* 🌐 LINKS */
function openGoogle(){
    window.open("https://google.com");
}

function openMaps(){
    window.open("https://maps.google.com");
}

</script>

</body>
</html>



"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def enviar_404(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"No encontrado")


if __name__ == "__main__":
    servidor = HTTPServer(("127.0.0.1", 9000), MiServidor)
    print("Servidor corriendo en http://localhost:9000")
    servidor.serve_forever()

