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
    --card:white;
    --text:#000;
    --input:#f9f9fb;
}

body.dark{
    --bg:#1c1c1e;
    --card:#2c2c2e;
    --text:#fff;
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
    border-radius:18px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

/* DARK BUTTON */
.dark-toggle{
    position:fixed;
    top:20px;
    right:20px;
    padding:8px 14px;
    border-radius:10px;
    border:none;
    cursor:pointer;
}

/* IC GRID 3x3 */
.ic-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:10px;
}

/* INPUT AUTO GROW */
.auto-grow{
    min-width:80px;
    width:80px;
    padding:6px;
    border-radius:8px;
    border:1px solid #ccc;
    background:var(--input);
    transition:.2s;
}
.auto-grow:focus{
    outline:none;
}
button{
    padding:8px 12px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    background:#e5e5ea;
}

/* FFI PREVIEW */
.ffi-preview{
    margin-top:20px;
    padding:20px;
    border-radius:16px;
    border:4px solid red;
    min-height:200px;
    white-space:pre-line;
}
strong{font-weight:700;}
</style>
</head>

<body>

<button class="dark-toggle" onclick="toggleDark()">🌙 Dark</button>

<h1>Alexa Builder 🚀</h1>

<!-- IC -->
<section>
<h2>IC</h2>

<div class="ic-grid">
<button onclick="addIC('YOB')">YOB</button>
<button onclick="addIC('@')">@</button>
<button onclick="addIC('Mobile Phone')">Mobile Phone</button>
<button onclick="addIC('OTP by txt')">OTP by txt</button>
<button onclick="addIC('OTP by @')">OTP by @</button>
<button onclick="addIC('UCID')">UCID</button>
</div>

<div id="resultIC"></div>
</section>

<!-- FFI -->
<section>
<h2>FFI</h2>

<input class="auto-grow" id="docInput" placeholder="Doc" oninput="grow(this);updatePreview()"><br><br>

<strong>60% Proxy</strong><br>
<button onclick="setProxy('Yes')">Yes</button>
<button onclick="setProxy('No')">No</button>
<button onclick="setProxy('NA')">NA</button>
<br><br>

Docs:
<input class="auto-grow" id="docsInput" oninput="grow(this);updatePreview()">

$
<input class="auto-grow" id="incomeInput" oninput="grow(this);updatePreview()">

%
<input class="auto-grow" id="percentInput" oninput="grow(this);updatePreview()">

<br><br>

<input class="auto-grow" id="reportInput" placeholder="Report" oninput="grow(this);updatePreview()"><br><br>
<input class="auto-grow" id="showingInput" placeholder="Showing" oninput="grow(this);updatePreview()"><br><br>
<input class="auto-grow" id="balanceInput" placeholder="Balance" oninput="grow(this);updatePreview()"><br><br>
<input class="auto-grow" id="outcomeInput" placeholder="Outcome" oninput="grow(this);updatePreview()">

<div class="ffi-preview" id="ffiPreview"></div>

</section>

<script>

/* DARK MODE */
function toggleDark(){
    document.body.classList.toggle("dark");
}

/* IC */
let icList=[];
function addIC(v){
    icList.push(v);
    document.getElementById("resultIC").innerText=
        "VID: "+icList.map(x=>x+" OK").join(" + ");
}

/* INPUT GROW */
function grow(input){
    input.style.width = (input.value.length + 2) + "ch";
}

/* FFI */
let selectedProxy="";
function setProxy(v){
    selectedProxy=v;
    updatePreview();
}

function updatePreview(){
    document.getElementById("ffiPreview").innerHTML =
`<strong>Doc:</strong> ${docInput.value}

<strong>60% Proxy:</strong> ${selectedProxy}
<strong>Docs:</strong> ${docsInput.value}
<strong>$:</strong> ${incomeInput.value}
<strong>%:</strong> ${percentInput.value}

<strong>Report:</strong> ${reportInput.value}
<strong>Showing:</strong> ${showingInput.value}
<strong>Balance:</strong> ${balanceInput.value}
<strong>Outcome:</strong> ${outcomeInput.value}`;
}

</script>

</body>
</html>
""" 