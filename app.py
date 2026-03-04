from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Alexa Builder</title>
<meta charset="UTF-8">

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
    --text:#ffffff;
    --input:#3a3a3c;
}

body{
    font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    background:var(--bg);
    color:var(--text);
    padding:30px;
    transition:0.3s;
}

.dark-toggle{
    position:fixed;
    top:20px;
    right:20px;
    padding:8px 14px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    background:#007aff;
    color:white;
    font-weight:600;
}

section{
    background:var(--card);
    padding:25px;
    margin-bottom:30px;
    border-radius:18px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

.top-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:30px;
    align-items:start;
}

@media(max-width:900px){
    .top-grid{ grid-template-columns:1fr; }
}

button{
    padding:8px 14px;
    margin:5px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    background:#e5e5ea;
    transition:all 0.2s ease;
}

button:hover{ transform:translateY(-2px); }
button:active{ transform:scale(0.96); }

.copy-success{ background:#34c759!important;color:white!important; }
.reset-flash{ background:#ff3b30!important;color:white!important; }

.proxy-green{ background:#34c759!important;color:white; }
.proxy-red{ background:#ff3b30!important;color:white; }
.proxy-yellow{ background:#ffcc00!important; }

.ic-grid{
    display:grid;
    grid-template-columns:repeat(3, auto);
    justify-content:center;
    gap:8px;
}

.ic-grid button{
    padding:5px 9px;
    font-size:12px;
    border-radius:20px;
}

.converter{
    display:flex;
    align-items:center;
    gap:10px;
    flex-wrap:wrap;
}

.swap{ font-size:18px; cursor:pointer; }
.copy-center{ text-align:center; margin-top:30px; }

input, select{
    padding:6px 8px;
    border-radius:10px;
    border:1px solid #d1d1d6;
    background:var(--input);
    color:var(--text);
    font-size:14px;
    width:2ch;
    min-width:3ch;
    max-width:300px;
    box-sizing:content-box;
}

/* ================= MODAL ================= */

.modal{
    display:none;
    position:fixed;
    z-index:1000;
    left:0;
    top:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.4);
    backdrop-filter:blur(4px);
}

.modal-content{
    background:var(--card);
    margin:5% auto;
    padding:30px;
    width:90%;
    max-width:500px;
    border-radius:20px;
    box-shadow:0 10px 40px rgba(0,0,0,0.2);
    animation:fadeModal 0.2s ease;
}

.close{
    float:right;
    font-size:22px;
    cursor:pointer;
    font-weight:bold;
}

@keyframes fadeModal{
    from{opacity:0; transform:translateY(-10px);}
    to{opacity:1; transform:translateY(0);}
}
</style>
</head>

<body>

<button class="dark-toggle" onclick="toggleDark()">🌙 Dark</button>
<h1>Alexa Builder 🚀</h1>

<div class="top-grid">

<section>
<h2>IC</h2>
<div class="ic-grid">
<button onclick="addIC('YOB')">YOB</button>
<button onclick="addIC('@')">@</button>
<button onclick="addIC('Mobile Phone')">Mobile Phone</button>
<button onclick="addIC('OTP by txt')">OTP by txt</button>
<button onclick="addIC('OTP by @')">OTP by @</button>
<button onclick="addIC('UCID')">UCID</button>
<button onclick="eraseIC()">←</button>
<button id="copyICBtn" onclick="copyIC()">Copy</button>
<button id="resetICBtn" onclick="resetIC()">Reset</button>
</div>
<div id="resultIC"></div>
</section>

<section>
<h2>Currency Converter</h2>
<div class="converter">
<input type="number" id="amount1" value="1" oninput="convert(1)">
<select id="currency1" onchange="convert(1)">
<option value="USD">USD</option>
<option value="MXN">MXN</option>
<option value="CAD">CAD</option>
</select>

<span class="swap" onclick="swapCurrencies()">⇄</span>

<input type="number" id="amount2" oninput="convert(2)">
<select id="currency2" onchange="convert(1)">
<option value="MXN">MXN</option>
<option value="USD">USD</option>
<option value="CAD">CAD</option>
</select>
</div>
</section>

<section>
<h2>Date Calculator</h2>
<input type="number" id="daysToAdd" min="0" placeholder="Days from today">
<button onclick="calculateDate()">Calculate</button>
<button onclick="quickAdd(18)">+18</button>
<button onclick="quickAdd(30)">+30</button>
<div id="resultDate"></div>
</section>

<section>
<h2>FFI</h2>
<button onclick="openFFI()">Open FFI Form</button>
</section>

</div>

<!-- MODAL FFI -->
<div id="ffiModal" class="modal">
<div class="modal-content">
<span class="close" onclick="closeFFI()">×</span>
<h2>FFI Form</h2>

<input type="text" id="docInput" placeholder="Doc"><br><br>

<strong>60% Proxy</strong><br>
<button id="proxyYes" onclick="setProxy('Yes')">Yes</button>
<button id="proxyNo" onclick="setProxy('No')">No</button>
<button id="proxyNA" onclick="setProxy('NA')">NA</button>

<br><br>

<input type="text" id="docsInput" placeholder="Docs">
<input type="number" id="incomeInput" placeholder="$">
<input type="number" id="percentInput" placeholder="%">

<br><br>

<input type="text" id="reportInput" placeholder="Report"><br><br>
<input type="text" id="showingInput" placeholder="Showing"><br><br>
<input type="text" id="balanceInput" placeholder="Balance"><br><br>
<input type="text" id="outcomeInput" placeholder="Outcome">

<div class="copy-center">
<button id="copyFFIBtn" onclick="copyFFI()">Copy FFI</button>
<button id="resetFFIBtn" onclick="resetFFI()">Reset</button>
</div>

</div>
</div>

<script>

function toggleDark(){
    document.body.classList.toggle("dark");
}

function copyFeedback(button){
    const original = button.innerText;
    button.classList.add("copy-success");
    button.innerText = "✓ Copied";
    setTimeout(()=>{
        button.classList.remove("copy-success");
        button.innerText = original;
    },2000);
}

function resetFeedback(button){
    button.classList.add("reset-flash");
    setTimeout(()=>{
        button.classList.remove("reset-flash");
    },1000);
}

function openFFI(){
    document.getElementById("ffiModal").style.display="block";
}

function closeFFI(){
    document.getElementById("ffiModal").style.display="none";
}

window.onclick=function(event){
    let modal=document.getElementById("ffiModal");
    if(event.target===modal){
        modal.style.display="none";
    }
}

let selectedProxy="";

function setProxy(value){
    selectedProxy=value;
    proxyYes.classList.remove("proxy-green","proxy-red","proxy-yellow");
    proxyNo.classList.remove("proxy-green","proxy-red","proxy-yellow");
    proxyNA.classList.remove("proxy-green","proxy-red","proxy-yellow");

    if(value==="Yes")proxyYes.classList.add("proxy-green");
    if(value==="No")proxyNo.classList.add("proxy-red");
    if(value==="NA")proxyNA.classList.add("proxy-yellow");
}

function copyFFI(){
    let text=`===========FFI===========
Doc: ${docInput.value}
60% Proxy: ${selectedProxy} ; ${docsInput.value} + $${incomeInput.value} + ${percentInput.value}%
Report: ${reportInput.value}
Showing: ${showingInput.value}
Balance: ${balanceInput.value}
Outcome: ${outcomeInput.value}
=======================`;
    navigator.clipboard.writeText(text);
    copyFeedback(document.getElementById("copyFFIBtn"));
}

function resetFFI(){
    selectedProxy="";
    ["docInput","docsInput","incomeInput","percentInput","reportInput","showingInput","balanceInput","outcomeInput"]
    .forEach(id=>document.getElementById(id).value="");

    proxyYes.classList.remove("proxy-green");
    proxyNo.classList.remove("proxy-red");
    proxyNA.classList.remove("proxy-yellow");

    resetFeedback(document.getElementById("resetFFIBtn"));
}

</script>
</body>
</html>
"""

