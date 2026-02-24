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

/* DARK BUTTON */
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
    .top-grid{
        grid-template-columns:1fr;
    }
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
    background:var(--input);
    color:var(--text);
    font-size:14px;
    width:auto;
    min-width:80px;
    max-width:100%;
}

input:focus,select:focus{
    outline:none;
    border:1px solid #007aff;
    background:white;
}

/* IC GRID 3x3 */
.ic-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:10px;
    margin-bottom:15px;
}

.success{ background:#34c759!important;color:white; }
.error{ background:#ff3b30!important;color:white; }

.proxy-green{ background:#34c759!important;color:white; }
.proxy-red{ background:#ff3b30!important;color:white; }
.proxy-yellow{ background:#ffcc00!important; }

.copy-center{
    text-align:center;
    margin-top:30px;
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
</div>

<div id="resultIC"></div>

<br>
<button onclick="eraseIC()">←</button>
<button id="copyICBtn" onclick="copyIC()">Copy</button>
<button onclick="resetIC()">Reset</button>
</section>

<div>

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

</div>
</div>

<script>

/* DARK MODE */
const darkBtn = document.querySelector(".dark-toggle");

function updateDarkButton(){
    darkBtn.innerHTML = document.body.classList.contains("dark") ? "🌞 Light" : "🌙 Dark";
}

function toggleDark(){
    document.body.classList.toggle("dark");
    updateDarkButton();
}

updateDarkButton();

/* AUTO RESIZE INPUTS */
document.querySelectorAll("input[type='text'], input[type='number']").forEach(input=>{
    function resize(){
        input.style.width = "auto";
        input.style.width = (input.scrollWidth + 10) + "px";
    }
    input.addEventListener("input", resize);
    resize();
});

/* DATE ENTER */
daysToAdd.addEventListener("keydown", function(e){
    if(e.key==="Enter"){ calculateDate(); }
});

/* IC */
let icList=[];
function updateIC(){
if(icList.length===0){resultIC.innerText="";return;}
resultIC.innerText="VID: "+icList.map(x=>x+" OK").join(" + ");
}
function addIC(v){icList.push(v);updateIC();}
function eraseIC(){icList.pop();updateIC();}
function resetIC(){icList=[];updateIC();}
function copyIC(){navigator.clipboard.writeText(resultIC.innerText);}

/* CURRENCY */
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

/* DATE */
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

</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)