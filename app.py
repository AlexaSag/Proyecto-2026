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
body{
    font-family:-apple-system,BlinkMacSystemFont,sans-serif;
    background:#f2f2f7;
    padding:30px;
}

/* GRID SUPERIOR */
.top-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:30px;
    align-items:start;
}

@media(max-width:900px){
    .top-grid{
        grid-template-columns:1fr;
    }
}

section{
    background:white;
    padding:25px;
    margin-bottom:30px;
    border-radius:18px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

h2{ margin-bottom:15px; }

button{
    padding:8px 14px;
    margin:5px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    background:#e5e5ea;
    transition:0.2s;
}

button:hover{ opacity:0.85; }

input,select{
    padding:10px;
    border-radius:10px;
    border:1px solid #d1d1d6;
    background:#f9f9fb;
    font-size:14px;
}

input:focus,select:focus{
    outline:none;
    border:1px solid #007aff;
    background:white;
}

.success{ background:#34c759!important;color:white; }
.error{ background:#ff3b30!important;color:white; }

.proxy-green{ background:#34c759!important;color:white; }
.proxy-red{ background:#ff3b30!important;color:white; }
.proxy-yellow{ background:#ffcc00!important; }

.ffi-box{
    background:white;
    padding:20px;
    border-radius:16px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

.ffi-row-bottom{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
    gap:20px;
    margin-top:15px;
}

.copy-center{
    text-align:center;
    margin-top:30px;
}

.custom-btn{
    background:#007aff;
    color:white;
    position:relative;
    margin:6px;
}

.delete-x{
    position:absolute;
    right:6px;
    top:2px;
    cursor:pointer;
    font-weight:bold;
}

.converter{
    display:flex;
    align-items:center;
    gap:10px;
    flex-wrap:wrap;
}

.swap{
    font-size:18px;
    cursor:pointer;
}
</style>
</head>

<body>

<h1>Alexa Builder 🚀</h1>

<div class="top-grid">

<!-- IC -->
<section>
<h2>IC</h2>
<button onclick="addIC('YOB')">YOB</button>
<button onclick="addIC('@')">@</button>
<button onclick="addIC('Mobile Phone')">Mobile Phone</button>
<button onclick="addIC('OTP by txt')">OTP by txt</button>
<button onclick="addIC('OTP by @')">OTP by @</button>
<button onclick="addIC('UCID')">UCID</button>
<div id="resultIC"></div>
<br>
<button onclick="eraseIC()">←</button>
<button id="copyICBtn" onclick="copyIC()">Copy</button>
<button onclick="resetIC()">Reset</button>
</section>

<!-- RIGHT COLUMN -->
<div>

<!-- Currency -->
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

<!-- DATE -->
<section>
<h2>Date Calculator</h2>
<input type="number" id="daysToAdd" min="0" placeholder="Days from today">
<button onclick="calculateDate()">Calculate</button>
<button onclick="quickAdd(18)">+18</button>
<button onclick="quickAdd(30)">+30</button>
<div id="resultDate"></div>
</section>

</div>
</div>

<!-- FFI -->
<section>
<h2>FFI</h2>

<input type="text" id="docInput" placeholder="Doc">

<div class="ffi-row-bottom">

<div>
<strong>60% Proxy</strong><br>
<button id="proxyYes" onclick="setProxy('Yes')">Yes</button>
<button id="proxyNo" onclick="setProxy('No')">No</button>
<button id="proxyNA" onclick="setProxy('NA')">NA</button>
</div>

<div>
<strong>Docs</strong><br>
<input type="text" id="docsInput">
</div>

<div>
<strong>$</strong><br>
<input type="number" id="incomeInput">
</div>

<div>
<strong>%</strong><br>
<input type="number" id="percentInput">
</div>

</div>

<br>
<input type="text" id="reportInput" placeholder="Report"><br><br>
<input type="text" id="showingInput" placeholder="Showing"><br><br>
<input type="text" id="balanceInput" placeholder="Balance"><br><br>
<input type="text" id="outcomeInput" placeholder="Outcome">

<div class="copy-center">
<button id="copyFFIBtn" onclick="copyFFI()">Copy FFI</button>
<button onclick="resetFFI()">Reset</button>
</div>
</section>

<!-- CUSTOM -->
<section>
<h2>Custom Buttons</h2>

<input type="text" id="customLabel" placeholder="Button Name">
<input type="text" id="customText" placeholder="Text to Copy">
<button onclick="createCustom()">Create</button>

<div id="customContainer"></div>

<br>
<button id="copyAllBtn" onclick="copyAllCustom()">Copy All</button>
<button onclick="resetCustom()">Reset</button>
</section>

<script>

/* IC */
let icList=[];
function updateIC(){
if(icList.length===0){document.getElementById("resultIC").innerText="";return;}
document.getElementById("resultIC").innerText="VID: "+icList.map(x=>x+" OK").join(" + ");
}
function addIC(v){icList.push(v);updateIC();}
function eraseIC(){icList.pop();updateIC();}
function resetIC(){icList=[];updateIC();}
function copyIC(){
let btn=document.getElementById("copyICBtn");
navigator.clipboard.writeText(document.getElementById("resultIC").innerText)
.then(()=>{btn.classList.add("success");setTimeout(()=>btn.classList.remove("success"),800);})
.catch(()=>{btn.classList.add("error");setTimeout(()=>btn.classList.remove("error"),800);});
}

/* CURRENCY */
const rates={USD:1,MXN:17,CAD:1.35};
function convert(from){
let a1=parseFloat(document.getElementById("amount1").value)||0;
let a2=parseFloat(document.getElementById("amount2").value)||0;
let c1=document.getElementById("currency1").value;
let c2=document.getElementById("currency2").value;
if(from===1){
let usd=a1/rates[c1];
document.getElementById("amount2").value=(usd*rates[c2]).toFixed(2);
}else{
let usd=a2/rates[c2];
document.getElementById("amount1").value=(usd*rates[c1]).toFixed(2);
}
}
function swapCurrencies(){
let c1=document.getElementById("currency1");
let c2=document.getElementById("currency2");
let temp=c1.value;c1.value=c2.value;c2.value=temp;
convert(1);
}
convert(1);

/* DATE */
function calculateDate(){
let days=parseInt(document.getElementById("daysToAdd").value);
if(isNaN(days)||days<0)return;
let today=new Date();
today.setDate(today.getDate()+days);
document.getElementById("resultDate").innerText=
(today.getMonth()+1)+"/"+today.getDate();
}
function quickAdd(days){
document.getElementById("daysToAdd").value=days;
calculateDate();
}

/* FFI */
let selectedProxy="";
function setProxy(value){
selectedProxy=value;
["proxyYes","proxyNo","proxyNA"].forEach(id=>document.getElementById(id).classList.remove("proxy-green","proxy-red","proxy-yellow"));
if(value==="Yes")document.getElementById("proxyYes").classList.add("proxy-green");
if(value==="No")document.getElementById("proxyNo").classList.add("proxy-red");
if(value==="NA")document.getElementById("proxyNA").classList.add("proxy-yellow");
}
function copyFFI(){
let btn=document.getElementById("copyFFIBtn");
let text=`===========FFI===========
Doc: ${docInput.value}
60% Proxy: ${selectedProxy} ; ${docsInput.value} + $${incomeInput.value} + ${percentInput.value}%
Report: ${reportInput.value}
Showing: ${showingInput.value}
Balance: ${balanceInput.value}
Outcome: ${outcomeInput.value}
=======================`;
navigator.clipboard.writeText(text)
.then(()=>{btn.classList.add("success");setTimeout(()=>btn.classList.remove("success"),800);})
.catch(()=>{btn.classList.add("error");setTimeout(()=>btn.classList.remove("error"),800);});
}
function resetFFI(){
selectedProxy="";
["docInput","docsInput","incomeInput","percentInput","reportInput","showingInput","balanceInput","outcomeInput"]
.forEach(id=>document.getElementById(id).value="");
}

/* CUSTOM */
let customList=[];
function createCustom(){
let label=customLabel.value;
let text=customText.value;
if(!label||!text)return;
let btn=document.createElement("button");
btn.className="custom-btn";
btn.innerText=label;
btn.onclick=function(){customList.push(text);navigator.clipboard.writeText(text);};
customContainer.appendChild(btn);
customLabel.value="";customText.value="";
}
function copyAllCustom(){
navigator.clipboard.writeText(customList.join(" + "));
}
function resetCustom(){
customList=[];customContainer.innerHTML="";
}

</script>
</body>
</html>
"""
