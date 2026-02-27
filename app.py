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
}

.success{ background:#34c759!important;color:white; }
.error{ background:#ff3b30!important;color:white; }

.proxy-green{ background:#34c759!important;color:white; }
.proxy-red{ background:#ff3b30!important;color:white; }
.proxy-yellow{ background:#ffcc00!important; }

.converter{
    display:flex;
    align-items:center;
    gap:10px;
    flex-wrap:wrap;
}
.swap{ font-size:18px; cursor:pointer; }
.copy-center{ text-align:center; margin-top:30px; }

/* IC GRID */
.ic-grid{
    display:grid;
    grid-template-columns:repeat(3, 1fr);
    gap:10px;
    margin-bottom:15px;
}

.ic-grid button{
    width:100%;
}

/* AUTO-RESIZE INPUTS */
input,select{
    padding:8px 10px;
    border-radius:10px;
    border:1px solid #d1d1d6;
    background:var(--input);
    color:var(--text);
    font-size:14px;
    width:auto;
    min-width:40px;
    max-width:100%;
    box-sizing:border-box;
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
<button onclick="resetIC()">Reset</button>
</div>

<div id="resultIC"></div>

</section>
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

</div>
</div>

<section>
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
<button onclick="copyFFI()">Copy FFI</button>
<button onclick="resetFFI()">Reset</button>
</div>
</section>

<section>
<h2>Custom Buttons</h2>
<input type="text" id="customLabel" placeholder="Button Name">
<input type="text" id="customText" placeholder="Text to Copy">
<button onclick="createCustom()">Create</button>
<div id="customContainer"></div>
<br>
<button onclick="copyAllCustom()">Copy All</button>
<button onclick="resetCustom()">Reset</button>
</section>

<script>

////////////////////////////////////////////////////
//// 1️⃣ DARK MODE ZONE
////////////////////////////////////////////////////

const darkBtn = document.querySelector(".dark-toggle");

function updateDarkButton(){
    darkBtn.innerHTML = document.body.classList.contains("dark")
        ? "🌞 Light"
        : "🌙 Dark";
}

function toggleDark(){
    document.body.classList.toggle("dark");
    updateDarkButton();
}

updateDarkButton();

////////////////////////////////////////////////////
//// 2️⃣ IC ZONE
////////////////////////////////////////////////////

let icList=[];

function updateIC(){
    const result=document.getElementById("resultIC");
    if(icList.length===0){ result.innerText=""; return; }
    result.innerText="VID: "+icList.map(x=>x+" OK").join(" + ");
}

function addIC(v){ icList.push(v); updateIC(); }
function eraseIC(){ icList.pop(); updateIC(); }
function resetIC(){ icList=[]; updateIC(); }

function copyIC(){
    navigator.clipboard.writeText(resultIC.innerText);
}

////////////////////////////////////////////////////
//// 3️⃣ CURRENCY ZONE
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

////////////////////////////////////////////////////
//// 4️⃣ DATE ZONE
////////////////////////////////////////////////////

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

////////////////////////////////////////////////////
//// 5️⃣ FFI ZONE
////////////////////////////////////////////////////

let selectedProxy="";

function setProxy(value){
    selectedProxy = value;

    const yes = document.getElementById("proxyYes");
    const no = document.getElementById("proxyNo");
    const na = document.getElementById("proxyNA");

    yes.classList.remove("proxy-green");
    no.classList.remove("proxy-red");
    na.classList.remove("proxy-yellow");

    if(value === "Yes") yes.classList.add("proxy-green");
    if(value === "No") no.classList.add("proxy-red");
    if(value === "NA") na.classList.add("proxy-yellow");
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
}

function resetFFI(){
    selectedProxy="";
    ["docInput","docsInput","incomeInput","percentInput","reportInput","showingInput","balanceInput","outcomeInput"]
    .forEach(id=>document.getElementById(id).value="");
}

////////////////////////////////////////////////////
//// 6️⃣ CUSTOM BUTTONS ZONE
////////////////////////////////////////////////////

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
}

function resetCustom(){
    customList=[];
    customContainer.innerHTML="";
}

////////////////////////////////////////////////////
//// AUTO RESIZE INPUTS ZONE
////////////////////////////////////////////////////

function autoResizeInput(input){
    input.style.width = "auto";
    input.style.width = (input.scrollWidth + 5) + "px";
}

function enableAutoResize(){
    document.querySelectorAll("input").forEach(input=>{
        autoResizeInput(input);
        input.addEventListener("input", function(){
            autoResizeInput(this);
        });
    });
}

enableAutoResize();




</script>
</body>
</html>
"""
