from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Alexa Builder</title>

<style>
:root{
    --bg:#f2f2f7;
    --card:#ffffff;
    --text:#000;
    --input:#f2f2f7;
}

body.dark{
    --bg:#1c1c1e;
    --card:#2c2c2e;
    --text:#ffffff;
    --input:#3a3a3c;
}

body{
    font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    background:var(--bg);
    color:var(--text);
    padding:30px;
    transition:.3s;
}

section{
    background:var(--card);
    padding:25px;
    margin-bottom:30px;
    border-radius:20px;
    box-shadow:0 8px 25px rgba(0,0,0,0.08);
}

/* DARK MODE BUTTON */
.dark-btn{
    position:fixed;
    top:20px;
    right:20px;
    padding:8px 14px;
    border:none;
    border-radius:12px;
    cursor:pointer;
}

/* INPUTS SMALL + AUTO GROW */
.auto{
    width:80px;
    min-width:80px;
    padding:8px;
    border-radius:12px;
    border:1px solid #ccc;
    background:var(--input);
    transition:.2s;
}
.auto:focus{ outline:none; }

/* IC GRID 3x3 */
.ic-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:10px;
    margin-bottom:10px;
}

button{
    padding:8px;
    border:none;
    border-radius:12px;
    background:#e5e5ea;
    cursor:pointer;
}

button:hover{opacity:.8;}

.ic-actions{
    margin-top:10px;
}

/* FFI PREVIEW (CUADRO ROJO) */
.preview-box{
    margin-top:20px;
    padding:25px;
    border-radius:18px;
    border:5px solid red;
    background:var(--card);
    min-height:220px;
    white-space:pre-line;
    font-size:20px;
}

strong{font-weight:700;}
</style>
</head>

<body>

<button class="dark-btn" onclick="toggleDark()">🌙 Dark</button>

<h1>Alexa Builder 🚀</h1>

<!-- IC -->
<section>
<h2>IC</h2>

<div class="ic-grid">
<button onclick="addIC('YOB')">YOB</button>
<button onclick="addIC('@')">@</button>
<button onclick="addIC('Mobile')">Mobile</button>
<button onclick="addIC('OTP txt')">OTP txt</button>
<button onclick="addIC('OTP @')">OTP @</button>
<button onclick="addIC('UCID')">UCID</button>
</div>

<div id="resultIC"></div>

<div class="ic-actions">
<button onclick="eraseIC()">←</button>
<button onclick="copyIC()">Copy</button>
<button onclick="resetIC()">Reset</button>
</div>

</section>

<!-- FFI -->
<section>
<h2>FFI</h2>

<input class="auto" id="doc" placeholder="Doc" oninput="grow(this);updateFFI()"><br><br>

<strong>60% Proxy</strong><br>
<button onclick="setProxy('Yes')">Yes</button>
<button onclick="setProxy('No')">No</button>
<button onclick="setProxy('NA')">NA</button>
<br><br>

Docs:
<input class="auto" id="docs" oninput="grow(this);updateFFI()">

$
<input class="auto" id="income" type="number" oninput="grow(this);updateFFI()">

%
<input class="auto" id="percent" type="number" oninput="grow(this);updateFFI()">

<br><br>

<input class="auto" id="report" placeholder="Report" oninput="grow(this);updateFFI()"><br><br>
<input class="auto" id="showing" placeholder="Showing" oninput="grow(this);updateFFI()"><br><br>
<input class="auto" id="balance" placeholder="Balance" oninput="grow(this);updateFFI()"><br><br>
<input class="auto" id="outcome" placeholder="Outcome" oninput="grow(this);updateFFI()">

<div class="preview-box" id="ffiPreview"></div>

</section>

<script>

/* DARK MODE */
function toggleDark(){
    document.body.classList.toggle("dark");
}

/* AUTO GROW */
function grow(el){
    el.style.width = (el.value.length + 2) + "ch";
}

/* IC */
let icList=[];
function addIC(v){
    icList.push(v);
    document.getElementById("resultIC").innerText =
        "VID: " + icList.map(x=>x+" OK").join(" + ");
}
function eraseIC(){
    icList.pop();
    addIC("");
}
function resetIC(){
    icList=[];
    document.getElementById("resultIC").innerText="";
}
function copyIC(){
    navigator.clipboard.writeText(document.getElementById("resultIC").innerText);
}

/* FFI */
let proxy="";

function setProxy(v){
    proxy=v;
    updateFFI();
}

function updateFFI(){
document.getElementById("ffiPreview").innerHTML =
`===========FFI===========

<strong>Doc:</strong> ${doc.value}
<strong>60% Proxy:</strong> ${docs.value} + $${income.value} + ${percent.value}%
<strong>Report:</strong> ${report.value}
<strong>Showing:</strong> ${showing.value}
<strong>Balance:</strong> ${balance.value}
<strong>Outcome:</strong> ${outcome.value}

=========================`;
}

</script>

</body>
</html>
"""
if __name__ == "__main__":
    app.run()



