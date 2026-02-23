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
body {
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background:#f2f2f7;
    padding:30px;
}

section {
    background:white;
    padding:25px;
    margin-bottom:30px;
    border-radius:18px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

h2 { margin-bottom:15px; }

button {
    padding:8px 14px;
    margin:5px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    background:#e5e5ea;
    transition:0.2s;
}

button:hover { opacity:0.85; }

input, select {
    padding:10px;
    border-radius:10px;
    border:1px solid #d1d1d6;
    background:#f9f9fb;
    font-size:14px;
}

input:focus, select:focus {
    outline:none;
    border:1px solid #007aff;
    background:white;
}

.result {
    margin-top:10px;
    font-weight:bold;
}

.success { background:#34c759 !important; color:white; }
.error { background:#ff3b30 !important; color:white; }

.proxy-green { background:#34c759 !important; color:white; }
.proxy-red { background:#ff3b30 !important; color:white; }
.proxy-yellow { background:#ffcc00 !important; }

.ffi-box {
    background:white;
    padding:20px;
    border-radius:16px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

.ffi-row-top { margin-bottom:15px; }

.ffi-row-bottom {
    display:flex;
    align-items:center;
    gap:15px;
    flex-wrap:wrap;
}

.ffi-input-small { width:120px; }
.ffi-input-medium { width:180px; }

.copy-center {
    text-align:center;
    margin-top:20px;
}

.custom-btn {
    background:#007aff;
    color:white;
    position:relative;
    margin:6px;
}

.delete-x {
    position:absolute;
    right:6px;
    top:2px;
    cursor:pointer;
    font-weight:bold;
}

.converter {
    display:flex;
    align-items:center;
    gap:10px;
    flex-wrap:wrap;
}

.swap {
    font-size:18px;
    cursor:pointer;
}
</style>
</head>

<body>

<h1>Alexa Builder 🚀</h1>

<!-- IC -->
<section>
<h2>IC</h2>

<button onclick="addIC('YOB')">YOB</button>
<button onclick="addIC('@')">@</button>
<button onclick="addIC('Mobile Phone')">Mobile Phone</button>
<button onclick="addIC('OTP by txt')">OTP by txt</button>
<button onclick="addIC('OTP by @')">OTP by @</button>
<button onclick="addIC('UCID')">UCID</button>

<div class="result" id="resultIC"></div>

<br>
<button onclick="eraseIC()">←</button>
<button id="copyICBtn" onclick="copyIC()">Copy</button>
<button onclick="resetIC()">Reset</button>
</section>

<!-- FFI -->
<section>
<h2>FFI </h2>

<div class="ffi-box">

<div class="ffi-row-top">
<input type="text" id="docInput" placeholder="Doc" class="ffi-input-medium">
</div>

<div class="ffi-row-bottom">

<div>
<strong>60% Proxy</strong><br>
<button id="proxyYes" onclick="setProxy('Yes')">Yes</button>
<button id="proxyNo" onclick="setProxy('No')">No</button>
<button id="proxyNA" onclick="setProxy('NA')">NA</button>
</div>

<div>
<strong>Docs</strong><br>
<input type="text" id="docsInput" class="ffi-input-medium">
</div>

<div>
<strong>$</strong><br>
<input type="number" id="incomeInput" class="ffi-input-small">
</div>

<div>
<strong>%</strong><br>
<input type="number" id="percentInput" class="ffi-input-small">
</div>

</div>

<div style="margin-top:25px;">
<strong>Report</strong><br>
<input type="text" id="reportInput" class="ffi-input-medium"><br><br>

<strong>Showing</strong><br>
<input type="text" id="showingInput" class="ffi-input-medium"><br><br>

<strong>Balance</strong><br>
<input type="text" id="balanceInput" class="ffi-input-medium"><br><br>

<strong>Outcome</strong><br>
<input type="text" id="outcomeInput" class="ffi-input-medium">
</div>

<div class="copy-center">
<button id="copyFFIBtn" onclick="copyFFI()">Copy FFI</button>
<button onclick="resetFFI()">Reset</button>
</div>

</div>
</section>

<!-- CUSTOM -->
<section>
<h2>Custom Buttons</h2>

<input type="text" id="customLabel" placeholder="Button Name">
<input type="text" id="customText" placeholder="Text to Copy">
<button onclick="createCustom()">Create</button>

<div id="customContainer"></div>
<div class="result" id="resultCustom"></div>

<br>
<button id="copyAllBtn" onclick="copyAllCustom()">Copy All</button>
<button onclick="resetCustom()">Reset</button>
</section>

<!-- DATE -->
<section>
<h2>Date Calculator</h2>

<input type="number" id="daysToAdd" min="0"
placeholder="Days from today"
onkeypress="if(event.key==='Enter') calculateDate()">

<button onclick="calculateDate()">Calculate</button>
<button onclick="quickAdd(18)">+18</button>
<button onclick="quickAdd(30)">+30</button>

<div class="result" id="resultDate"></div>
</section>

<!-- CURRENCY -->
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

/* FFI */
let selectedProxy="";

function setProxy(value){
selectedProxy=value;

document.getElementById("proxyYes").classList.remove("proxy-green");
document.getElementById("proxyNo").classList.remove("proxy-red");
document.getElementById("proxyNA").classList.remove("proxy-yellow");

if(value==="Yes") document.getElementById("proxyYes").classList.add("proxy-green");
if(value==="No") document.getElementById("proxyNo").classList.add("proxy-red");
if(value==="NA") document.getElementById("proxyNA").classList.add("proxy-yellow");
}

function copyFFI(){
let btn=document.getElementById("copyFFIBtn");

let doc=document.getElementById("docInput").value||"";
let docs=document.getElementById("docsInput").value||"";
let income=document.getElementById("incomeInput").value||"";
let percent=document.getElementById("percentInput").value||"";
let report=document.getElementById("reportInput").value||"";
let showing=document.getElementById("showingInput").value||"";
let balance=document.getElementById("balanceInput").value||"";
let outcome=document.getElementById("outcomeInput").value||"";

let text=
`===========FFI===========
Doc: ${doc}
60% Proxy: ${selectedProxy} ; ${docs} + $${income} + ${percent}%
Report: ${report}
Showing: ${showing}
Balance: ${balance}
Outcome: ${outcome}
=======================`;

navigator.clipboard.writeText(text)
.then(()=>{btn.classList.add("success");setTimeout(()=>btn.classList.remove("success"),800);})
.catch(()=>{btn.classList.add("error");setTimeout(()=>btn.classList.remove("error"),800);});
}

function resetFFI(){
selectedProxy="";
document.getElementById("proxyYes").classList.remove("proxy-green");
document.getElementById("proxyNo").classList.remove("proxy-red");
document.getElementById("proxyNA").classList.remove("proxy-yellow");

["docInput","docsInput","incomeInput","percentInput",
"reportInput","showingInput","balanceInput","outcomeInput"]
.forEach(id=>document.getElementById(id).value="");
}

/* CUSTOM */
let customList=[];
function createCustom(){
let label=document.getElementById("customLabel").value;
let text=document.getElementById("customText").value;
if(!label||!text)return;

let btn=document.createElement("button");
btn.className="custom-btn";
btn.innerText=label;

let del=document.createElement("span");
del.innerText="×";
del.className="delete-x";
del.onclick=function(e){e.stopPropagation();customList=customList.filter(x=>x!==text);btn.remove();};
btn.appendChild(del);

btn.onclick=function(){
customList.push(text);
document.getElementById("resultCustom").innerText=customList.join(" + ");
navigator.clipboard.writeText(text);
};

document.getElementById("customContainer").appendChild(btn);
document.getElementById("customLabel").value="";
document.getElementById("customText").value="";
}
function copyAllCustom(){
let btn=document.getElementById("copyAllBtn");
navigator.clipboard.writeText(customList.join(" + "))
.then(()=>{btn.classList.add("success");setTimeout(()=>btn.classList.remove("success"),800);})
.catch(()=>{btn.classList.add("error");setTimeout(()=>btn.classList.remove("error"),800);});
}
function resetCustom(){
customList=[];
document.getElementById("customContainer").innerHTML="";
document.getElementById("resultCustom").innerText="";
}

/* DATE */
function formatDate(d){
let m=(d.getMonth()+1).toString().padStart(2,"0");
let day=d.getDate().toString().padStart(2,"0");
return m+"/"+day;
}
function calculateDate(){
let days=parseInt(document.getElementById("daysToAdd").value);
if(isNaN(days)||days<0)return;
let today=new Date();
today.setDate(today.getDate()+days);
document.getElementById("resultDate").innerText=formatDate(today);
}
function quickAdd(days){
document.getElementById("daysToAdd").value=days;
calculateDate();
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

</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)