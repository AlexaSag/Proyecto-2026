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

/* FFI MODAL */

.ffi-modal{
    display:none;
    position:fixed;
    inset:0;
    background:rgba(0,0,0,0.4);
    backdrop-filter:blur(6px);
    justify-content:center;
    align-items:center;
    z-index:1000;
}

.ffi-content{
    background:var(--card);
    padding:30px;
    border-radius:20px;
    width:90%;
    max-width:500px;
    max-height:90vh;
    overflow:auto;
    position:relative;
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
}

.close-btn{
    position:absolute;
    top:15px;
    right:20px;
    cursor:pointer;
    font-size:18px;
}



/* =========================
   GLOBAL BUTTON SYSTEM
========================= */

button{
    padding:8px 14px;
    margin:5px;
    border:none;
    border-radius:10px;
    cursor:pointer;
    background:#e5e5ea;
    transition:all 0.2s ease;
}

button:hover{
    transform:translateY(-2px);
}

button:active{
    transform:scale(0.96);
}

.copy-success{
    background:#34c759!important;
    color:white!important;
}

.reset-flash{
    background:#ff3b30!important;
    color:white!important;
}

/* Proxy colors */

.proxy-green{ background:#34c759!important;color:white; }
.proxy-red{ background:#ff3b30!important;color:white; }
.proxy-yellow{ background:#ffcc00!important; }

/* IC Animation */

.fade-in{
    opacity:1;
    transform:translateY(0);
}

.fade-out{
    opacity:0;
    transform:translateY(-5px);
}

.result-animated{
    transition:all 0.2s ease;
}

/* Layout */

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

/* ===== CURRENCY CLEAN LAYOUT ===== */

.converter{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:8px;
    flex-wrap:nowrap;
}

.currency-input{
    width:70px !important;
    min-width:70px !important;
    text-align:center;
}

.currency-select{
    width:85px;
    min-width:85px;
    padding:6px 8px;
    border-radius:10px;
    border:1px solid #d1d1d6;
    background:var(--input);
    color:var(--text);
    font-size:14px;
}

.swap{
    font-size:18px;
    cursor:pointer;
    padding:4px 8px;
    border-radius:50%;
    transition:0.2s;
}

.swap:hover{
    transform:rotate(180deg);
}
/* ===== CURRENCY end ===== */

.swap{ font-size:18px; cursor:pointer; }
.copy-center{ text-align:center; margin-top:30px; }

/* Auto resize */

input, select{
    padding:6px 8px;
    border-radius:10px;
    border:1px solid #d1d1d6;
    background:var(--input);
    color:var(--text);
    font-size:14px;

    width:2ch;              /* inicia ultra pequeño */
    min-width:auto;          /* mínimo real */
    max-width:300px;        /* evita que se vuelva gigante */
    box-sizing:content-box; /* importante */
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

<div id="resultIC" class="result-animated fade-in"></div>
</section>

<section>
<h2>Currency Converter</h2>

<div class="converter">

  <input type="number" id="amount1" value="1" oninput="convert(1)" class="currency-input">

  <select id="currency1" onchange="convert(1)" class="currency-select">
    <option value="USD">USD $</option>
    <option value="MXN">MXN $</option>
    <option value="CAD">CAD $</option>
  </select>

  <span class="swap" onclick="swapCurrencies()">⇄</span>

  <input type="number" id="amount2" oninput="convert(2)" class="currency-input">

  <select id="currency2" onchange="convert(1)" class="currency-select">
    <option value="MXN">MXN $</option>
    <option value="USD">USD $</option>
    <option value="CAD">CAD $</option>
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

</div>

<section>
<h2>Templates</h2>

<button onclick="openFFI()">Open FFI</button>

<button id="firstBtn" onclick="proximamente()">FIRST</button>

</section>

<!-- FFI MODAL -->
<div id="ffiModal" class="ffi-modal">
  <div class="ffi-content">

    <span class="close-btn" onclick="closeFFI()">✖</span>

    <h2>FFI</h2>

    <input type="text" id="docInput" placeholder="Doc">

    <div>
      <strong>60% Proxy</strong><br>
      <button id="proxyYes" onclick="setProxy('Yes')">Yes</button>
      <button id="proxyNo" onclick="setProxy('No')">No</button>
      <button id="proxyNA" onclick="setProxy('NA')">NA</button>
    </div>

    <br>

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

<section>
<h2>Custom Buttons</h2>
<input type="text" id="customLabel" placeholder="Button Name">
<input type="text" id="customText" placeholder="Text to Copy">
<button onclick="createCustom()">Create</button>
<div id="customContainer"></div>
<br>
<button id="copyAllCustomBtn" onclick="copyAllCustom()">Copy All</button>
<button id="resetCustomBtn" onclick="resetCustom()">Reset</button>
</section>




<script>

////////////////////////////////////////////////////
//// GLOBAL BUTTON FEEDBACK
////////////////////////////////////////////////////

function copyFeedback(button){
    const original = button.innerText;
    button.classList.add("copy-success");
    button.innerText = "✓ Copied";
    setTimeout(()=>{
        button.classList.remove("copy-success");
        button.innerText = original;
    },3000);
}

function resetFeedback(button){
    button.classList.add("reset-flash");
    setTimeout(()=>{
        button.classList.remove("reset-flash");
    },1000);
}

////////////////////////////////////////////////////
//// DARK MODE
////////////////////////////////////////////////////

const darkBtn=document.querySelector(".dark-toggle");

function updateDarkButton(){
    darkBtn.innerHTML=document.body.classList.contains("dark")
        ?"🌞 Light":"🌙 Dark";
}

function toggleDark(){
    document.body.classList.toggle("dark");
    updateDarkButton();
}
updateDarkButton();

////////////////////////////////////////////////////
//// IC ZONE
////////////////////////////////////////////////////

let icList=[];

function updateIC(){
    const result=document.getElementById("resultIC");
    if(icList.length===0){
        result.innerText="";
        return;
    }
    result.classList.remove("fade-out");
    result.classList.add("fade-in");
    result.innerText="VID: "+icList.map(x=>x+" OK").join(" + ");
}

function addIC(v){ icList.push(v); updateIC(); }

function eraseIC(){
    if(icList.length===0)return;
    const result=document.getElementById("resultIC");
    result.classList.remove("fade-in");
    result.classList.add("fade-out");
    setTimeout(()=>{
        icList.pop();
        updateIC();
    },150);
}

function resetIC(){
    icList=[];
    document.getElementById("resultIC").innerText="";
    resetFeedback(document.getElementById("resetICBtn"));
}

function copyIC(){
    if(icList.length===0)return;
    const text="VID: "+icList.map(x=>x+" OK").join(" + ");
    navigator.clipboard.writeText(text);
    copyFeedback(document.getElementById("copyICBtn"));
}

////////////////////////////////////////////////////
//// RESTO ORIGINAL (Currency, Date, Custom)
////////////////////////////////////////////////////

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

function swapCurrencies(){
    let temp=currency1.value;
    currency1.value=currency2.value;
    currency2.value=temp;
    convert(1);
}

convert(1);

function calculateDate(){
    let days=parseInt(daysToAdd.value);
    if(isNaN(days)||days<0)return;
    let today=new Date();
    today.setDate(today.getDate()+days);
    resultDate.innerText=(today.getMonth()+1)+"/"+today.getDate();
}

function quickAdd(days){
    daysToAdd.value=days;
    calculateDate();
}

let selectedProxy="";

function setProxy(value){
    selectedProxy=value;
    proxyYes.classList.remove("proxy-green");
    proxyNo.classList.remove("proxy-red");
    proxyNA.classList.remove("proxy-yellow");
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

    // Limpiar inputs
    ["docInput","docsInput","incomeInput","percentInput",
     "reportInput","showingInput","balanceInput","outcomeInput"]
    .forEach(id=>document.getElementById(id).value="");

    // 🔴 QUITAR selección visual de Proxy
    proxyYes.classList.remove("proxy-green");
    proxyNo.classList.remove("proxy-red");
    proxyNA.classList.remove("proxy-yellow");

    resetFeedback(document.getElementById("resetFFIBtn"));
}

let customList=[];

function createCustom(){
    let label=customLabel.value;
    let text=customText.value;
    if(!label||!text)return;

    let btn=document.createElement("button");
    btn.innerText=label;
    btn.onclick=function(){
        customList.push(text);
        navigator.clipboard.writeText(text);
    };

    customContainer.appendChild(btn);
    customLabel.value="";
    customText.value="";
}

function copyAllCustom(){
    navigator.clipboard.writeText(customList.join(" + "));
    copyFeedback(document.getElementById("copyAllCustomBtn"));
}

function resetCustom(){
    customList=[];
    customContainer.innerHTML="";
    resetFeedback(document.getElementById("resetCustomBtn"));
}

function autoResizeInput(input){
    const temp = document.createElement("span");
    temp.style.visibility = "hidden";
    temp.style.position = "absolute";
    temp.style.whiteSpace = "pre";
    temp.style.fontSize = getComputedStyle(input).fontSize;
    temp.style.fontFamily = getComputedStyle(input).fontFamily;

    temp.innerText = input.value || input.placeholder || "";

    document.body.appendChild(temp);

    input.style.width = (temp.offsetWidth + 15) + "px";

    document.body.removeChild(temp);
}

function enableAutoResize(){
    document.querySelectorAll("input").forEach(input=>{
        autoResizeInput(input);
        input.addEventListener("input", function(){
            autoResizeInput(this);
        });
    });
}

////////////////////////////////////////////////////
//// FFI MODAL CONTROL
////////////////////////////////////////////////////

function openFFI(){
    document.getElementById("ffiModal").style.display="flex";
}

function closeFFI(){
    document.getElementById("ffiModal").style.display="none";
}
function proximamente(){
    const btn = document.getElementById("firstBtn");
    btn.innerText = "Próximamente";
    btn.disabled = true; // opcional: lo desactiva
}
enableAutoResize();

</script>
</body>
</html>
"""
