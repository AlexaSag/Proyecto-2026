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

/* MICRO INTERACTIONS */

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
}

@media(max-width:900px){
    .top-grid{grid-template-columns:1fr;}
}

.ic-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:10px;
    margin-bottom:15px;
}

.ic-grid button{
    width:100%;
}

input,select{
    padding:8px 10px;
    border-radius:10px;
    border:1px solid #d1d1d6;
    background:var(--input);
    color:var(--text);
    font-size:14px;
    width:auto;
    min-width:40px;
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

</div>

<script>

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
//// IC ZONE PREMIUM UX
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

function addIC(v){
    icList.push(v);
    updateIC();
}

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
    const result=document.getElementById("resultIC");
    const btn=document.getElementById("resetICBtn");

    result.classList.remove("fade-in");
    result.classList.add("fade-out");
    result.innerText="";

    btn.classList.add("reset-flash");

    setTimeout(()=>{
        btn.classList.remove("reset-flash");
    },1000);
}

function copyIC(){
    if(icList.length===0)return;

    const text="VID: "+icList.map(x=>x+" OK").join(" + ");
    navigator.clipboard.writeText(text);

    const btn=document.getElementById("copyICBtn");
    const original=btn.innerText;

    btn.classList.add("copy-success");
    btn.innerText="✓ Copied";

    setTimeout(()=>{
        btn.classList.remove("copy-success");
        btn.innerText=original;
    },3000);
}

////////////////////////////////////////////////////
//// AUTO RESIZE
////////////////////////////////////////////////////

function autoResizeInput(input){
    input.style.width="auto";
    input.style.width=(input.scrollWidth+5)+"px";
}

function enableAutoResize(){
    document.querySelectorAll("input").forEach(input=>{
        autoResizeInput(input);
        input.addEventListener("input",function(){
            autoResizeInput(this);
        });
    });
}
enableAutoResize();

</script>
</body>
</html>
"""