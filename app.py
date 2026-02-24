from flask import Flask
import os

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
    --text:black;
    --input:#f9f9fb;
}

body.dark{
    --bg:#1c1c1e;
    --card:#2c2c2e;
    --text:white;
    --input:#3a3a3c;
}

body{
    font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    background:var(--bg);
    color:var(--text);
    padding:30px;
    transition:.3s;
}

.dark-toggle{
    position:fixed;
    top:20px;
    right:20px;
    padding:8px 14px;
    border:none;
    border-radius:10px;
    cursor:pointer;
}

.top-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:30px;
}

@media(max-width:900px){
    .top-grid{grid-template-columns:1fr;}
}

section{
    background:var(--card);
    padding:25px;
    margin-bottom:30px;
    border-radius:18px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

button{
    padding:8px 14px;
    margin:5px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    background:#e5e5ea;
}

.ic-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:10px;
}

.auto-grow{
    width:80px;
    min-width:80px;
    padding:6px;
    border-radius:10px;
    border:1px solid #ccc;
    background:var(--input);
}

input:focus{outline:none;border:1px solid #007aff;}

.preview-box{
    margin-top:20px;
    padding:25px;
    border-radius:16px;
    border:4px solid red;
    min-height:220px;
    white-space:pre-line;
    font-size:18px;
}

.success{ background:#34c759!important;color:white; }
.error{ background:#ff3b30!important;color:white; }
.proxy-green{ background:#34c759!important;color:white; }
.proxy-red{ background:#ff3b30!important;color:white; }
.proxy-yellow{ background:#ffcc00!important; }
</style>
</head>

<body>

<button class="dark-toggle" onclick="toggleDark()">🌙 Dark</button>

<h1>Alexa Builder 🚀</h1>

<div class="top-grid">

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

<div>
<button onclick="eraseIC()">←</button>
<button id="copyICBtn" onclick="copyIC()">Copy</button>
<button onclick="resetIC()">Reset</button>
</div>

</section>

<!-- RIGHT COLUMN -->
<div>

<section>
<h2>Currency Converter</h2>
<input type="number" id="amount1" value="1" oninput="convert(1)">
<select id="currency1" onchange="convert(1)">
<option value="USD">USD</option>
<option value="MXN">MXN</option>
<option value="CAD">CAD</option>
</select>
⇄
<input type="number" id="amount2" oninput="convert(2)">
<select id="currency2" onchange="convert(1)">
<option value="MXN">MXN</option>
<option value="USD">USD</option>
<option value="CAD">CAD</option>
</select>
</section>

<section>
<h2>Date Calculator</h2>
<input type="number" id="daysToAdd" min="0" placeholder="Days from today">
<button onclick="calculateDate()">Calculate</button>
<div id="resultDate"></div>
</section>

</div>
</div>

<!-- FFI -->
<section>
<h2>FFI</h2>

<input class="auto-grow" id="docInput" placeholder="Doc" oninput="grow(this);updatePreview()">

<div>
<strong>60% Proxy</strong><br>
<button id="proxyYes" onclick="setProxy('Yes')">Yes</button>
<button id="proxyNo" onclick="setProxy('No')">No</button>
<button id="proxyNA" onclick="setProxy('NA')">NA</button>
</div>

Docs <input class="auto-grow" id="docsInput" oninput="grow(this);updatePreview()">
$ <input class="auto-grow" id="incomeInput" oninput="grow(this);updatePreview()">
% <input class="auto-grow" id="percentInput" oninput="grow(this);updatePreview()">

<br><br>

<input class="auto-grow" id="reportInput" placeholder="Report" oninput="grow(this);updatePreview()"><br><br>
<input class="auto-grow" id="showingInput" placeholder="Showing" oninput="grow(this);updatePreview()"><br><br>
<input class="auto-grow" id="balanceInput" placeholder="Balance" oninput="grow(this);updatePreview()"><br><br>
<input class="auto-grow" id="outcomeInput" placeholder="Outcome" oninput="grow(this);updatePreview()">

<div class="preview-box" id="ffiPreview"></div>

</section>

<script>

/* DARK */
function toggleDark(){document.body.classList.toggle("dark");}

/* AUTO GROW */
function grow(el){el.style.width=(el.value.length+2)+"ch";}

/* IC */
let icList=[];
function updateIC(){
document.getElementById("resultIC").innerText=
icList.length? "VID: "+icList.map(x=>x+" OK").join(" + "):"";
}
function addIC(v){icList.push(v);updateIC();}
function eraseIC(){icList.pop();updateIC();}
function resetIC(){icList=[];updateIC();}
function copyIC(){navigator.clipboard.writeText(resultIC.innerText);}

/* Currency */
const rates={USD:1,MXN:17,CAD:1.35};
function convert(from){
let a1=parseFloat(amount1.value)||0;
let a2=parseFloat(amount2.value)||0;
let c1=currency1.value;
let c2=currency2.value;
if(from===1){
let usd=a1/rates[c1];
amount2.value=(usd*rates[c2]).toFixed(2);
}else{
let usd=a2/rates[c2];
amount1.value=(usd*rates[c1]).toFixed(2);
}
}
convert(1);

/* Date */
function calculateDate(){
let days=parseInt(daysToAdd.value);
if(isNaN(days))return;
let d=new Date();
d.setDate(d.getDate()+days);
resultDate.innerText=(d.getMonth()+1)+"/"+d.getDate();
}

/* FFI */
let selectedProxy="";
function setProxy(v){
selectedProxy=v;
["proxyYes","proxyNo","proxyNA"].forEach(id=>document.getElementById(id).classList.remove("proxy-green","proxy-red","proxy-yellow"));
if(v==="Yes")proxyYes.classList.add("proxy-green");
if(v==="No")proxyNo.classList.add("proxy-red");
if(v==="NA")proxyNA.classList.add("proxy-yellow");
updatePreview();
}

function updatePreview(){
ffiPreview.innerHTML=
`===========FFI===========

<strong>Doc:</strong> ${docInput.value}
<strong>60% Proxy:</strong> ${docsInput.value} + $${incomeInput.value} + ${percentInput.value}%
<strong>Report:</strong> ${reportInput.value}
<strong>Showing:</strong> ${showingInput.value}
<strong>Balance:</strong> ${balanceInput.value}
<strong>Outcome:</strong> ${outcomeInput.value}

=========================`;
}

</script>

</body>
</html>
"""
