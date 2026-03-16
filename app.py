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

/* DATE FIX DEFINITIVO */
#baseDate{
    width: 180px !important;
    min-width: 180px !important;
    box-sizing: border-box !important;
    flex-shrink: 0;
}

</style>
</head>

<body>

<button class="dark-toggle" onclick="toggleDark()">🌙 Dark</button>
<section>
<h2>Notes</h2>

<pre style="
background:#fff8c5;
border-left:5px solid #ffcc00;
padding:15px;
border-radius:10px;
font-size:14px;
">

<!DOCTYPE html>
<html>
<head>
<title>S.A.🧠</title>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>


<style>
:root{
    --bg:#f2f2f7;
    --card:white;
    --text:#000;
    --input:#f9f9fb;
}
h2{
font-size:18px;
margin-bottom:12px;
font-weight:600;
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
    padding:5px;
    transition:0.3s;
}
*{
    max-width:100%;
    box-sizing:border-box;
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
padding:18px;
margin-bottom:16px;
border-radius:20px;
box-shadow:0 8px 24px rgba(0,0,0,0.08);
    overflow:hidden;   /* 🔴 evita que se salgan */
}


h1{
    margin-bottom:15px;
}

.top-grid{
display:grid;
grid-template-columns:repeat(auto-fill,minmax(320px,1fr));
gap:14px;
align-items:start;
grid-auto-flow:dense;     /*grid-auto-flow:dense;*/
}



@media(max-width:900px){
    .top-grid{ grid-template-columns:1fr; }
}

/* FFI MODAL */
.ffi-modal{
    display:none;
    position:fixed;
    top:120px;
    right:20px;
    z-index:1000;   
}
.ffi-content{
    animation:modalPop .18s ease;
    background:#1c1c1e;
    padding:20px;
    border-radius:18px;
    color:white;   /* letras blancas */
    box-shadow:0 15px 40px rgba(0,0,0,0.35);
}

@keyframes modalPop{
0%{transform:scale(.92);opacity:.4;}
100%{transform:scale(1);opacity:1;}
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
border:none;
border-radius:12px;
cursor:pointer;
background:#e5e5ea;
transition:.2s ease;
font-weight:500;
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
/* TITULO SELECCION*/
.title-selected{
background:#007aff!important;
color:white!important;
}

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

/* ic y dark mode */
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
    background:#3a3a3c;
    color:white;
}

.top-right-buttons{
    display:flex;
    justify-content:flex-end;
    gap:10px;
    margin-bottom:10px;
}
.ic-toggle{
    position:fixed;
    top:50px;   /* debajo del Dark */
    right:20px;
    padding:8px 16px;
    border:none;
    border-radius:12px;
    cursor:pointer;
    font-weight:600;
    background:#ffd60a;
    color:#1c1c1e;
    transition:all .2s ease;
}
.ic-toggle:hover{
    transform:translateY(-2px);
}
.ic-toggle:active{
    transform:scale(.96);
}
/* ===== CURRENCY CLEAN LAYOUT ===== */
.converter{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:8px;
    flex-wrap:wrap; /* 🔴 permite acomodarse */
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
input:not(#daysToAdd):not(#baseDate), select{
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
#daysToAdd{ /* BOX DONDE ESCRIBES-4 O 7 */
    width:120px;
    min-width:120px;
}
/* ===== DATE FIX DEFINITIVO ===== */
#baseDate{
    width: 180px !important;
    min-width: 180px !important;
    box-sizing: border-box !important;
    flex-shrink: 0;
}
/* BASURERO */
#customContainer{
    display:flex;
    flex-wrap:wrap;
}
/* ===== CALENDARIO ===== */
.flatpickr-calendar{
    box-shadow:none;
}
.flatpickr-input{
    display:none !important;
}
.result-day{
    border:2px solid #007aff;
    background:#e8f2ff;
    color:#007aff;
    border-radius:50%;
}
.date-layout{
    display:flex;
    gap:15px;
    align-items:flex-start;
    flex-wrap:wrap;
}
.date-controls{
    display:flex;
    flex-direction:column;
    gap:5px;
    min-width:230px;
    align-self:flex-start;
    flex-shrink:0;
}
#dateResult{
display:inline-block;
padding:10px 18px;
font-size:25px;
font-weight:700;
border-radius:14px;
background:#007aff;
color:white;
margin-top:10px;
box-shadow:0 4px 10px rgba(0,0,0,0.15);
animation:pop .25s ease;
}
@keyframes pop{
0%{transform:scale(.8);opacity:.5;}
100%{transform:scale(1);opacity:1;}
}
#baseInfo{
font-size:18px;
font-weight:600;
margin-bottom:8px;
color:#555;
}
#dateResult{
text-align:center;
align-self:flex-start;
} 

/* ===== Oculta el selector del año (el cuadro con 20 y flechas) ===== */
.flatpickr-current-month .numInputWrapper{
    display:none !important;
}
/* ===== Oculta el texto del año ===== */
.flatpickr-current-month .cur-year{
    display:none !important;
}
.flatpickr-current-month{
    justify-content:center;
}
.quick-press{
transform:scale(.9);
background:#007aff;
color:white;
}
.template-buttons{
display:grid;
grid-template-columns:repeat(auto-fill,minmax(120px,1fr));
column-gap:10px;
row-gap:20px;   /* ← separación vertical real */
margin-top:8px;
}
.template-buttons button{
padding:10px 14px;
border-radius:10px;
line-height:1.3;
}
section:first-of-type button{
margin:3px;
}
/* ===============        NOTE          =============== */
.note-toggle{
    position:fixed;
    top:80px;   /* debajo de IC */
    right:20px;
    width:42px;
    height:42px;
    border:none;
    border-radius:12px;
    background:#e5e5ea;
    font-size:18px;
    cursor:pointer;
    display:flex;
    align-items:center;
    justify-content:center;
    transition:all .2s ease;
}
.note-toggle:hover{
    transform:translateY(-2px);
}
.note-toggle:active{
    transform:scale(.95);
}
.note-panel textarea{
width:100%;
min-height:80px;
max-height:350px;

border:none;
border-radius:12px;

padding:10px;

resize:none;
overflow:hidden;

background:#2c2c2e;
color:white;

font-family:inherit;
font-size:14px;
line-height:1.4;
}
.note-panel textarea{
width:100%;
height:80px;
border:none;
border-radius:10px;
padding:8px;
resize:none;
}
.note-buttons{
display:flex;
justify-content:space-between;
margin-top:8px;
}
.note-close{
position:absolute;
top:10px;
right:12px;

width:24px;
height:24px;

border-radius:50%;
background:#ff3b30;
color:white;

font-size:13px;

display:flex;
align-items:center;
justify-content:center;

cursor:pointer;
transition:.2s;
}

.note-close:hover{
transform:scale(1.1);
}
.note-panel textarea{
width:100%;
min-height:80px;
max-height:300px;
border:none;
border-radius:10px;
padding:10px;
resize:none;
overflow:hidden;
font-family:inherit;
font-size:14px;
}
.note-panel{
position:fixed;
top:120px;
right:20px;

background:#1c1c1e;
color:white;

padding:18px;
border-radius:18px;

box-shadow:0 20px 45px rgba(0,0,0,0.35);

width:260px;
max-width:420px;

display:none;
transition:all .2s ease;
}
/* ===============                  =============== */
/* ===============       BODY       =============== */
/* ===============                  =============== */
</style>
</head>
<body>
<div class="top-right-buttons">
    <button class="ic-toggle" onclick="toggleIC()">IC</button>
    <button class="dark-toggle" onclick="toggleDark()">🌙 Dark</button>
    <button class="note-toggle" id="noteToggle">📝</button>
</div>
<h1>S.A.🧠</h1>
<!------       IC MODAL (fuera del grid)       ------>
<div id="icModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeIC()">✖</span>
    <h2>IC</h2>
<div class="ic-grid"> <!-------- botones IC -------->
<button onclick="addIC('EAD')">📧</button>
<button onclick="addIC('MOB')">📱M</button>
<button onclick="addIC('WPH')">📞W</button>
<button onclick="addIC('YOB')">YOB</button>
<button onclick="addIC('CID')">CID</button>
<button onclick="addIC('CPW')">CPW</button>
<button onclick="addIC('3CSC')">3CSC</button>
<button onclick="addIC('ARC')">ARC</button>
<button onclick="addIC('BA')">ADDRESS</button>
<button onclick="addIC('OTP by txt')">OTP by txt</button>
<button onclick="addIC('OTP by @')">OTP by @</button>
<button onclick="addIC('TRANSFER CALL UCID')">UCID</button>
<button onclick="eraseIC()">←</button>
<button id="copyICBtn" onclick="copyIC()">Copy</button>
<button id="resetICBtn" onclick="resetIC()">Reset</button>
</div>

<div id="resultIC" class="result-animated fade-in"></div>
</div>
</div>
<!-------- GRID PRINCIPAL -------->
<div class="top-grid">

<!-- ================= TEMPLATES (PRIMERO) ================= -->
<section>
<h2>Templates</h2>
<button id="fdlBtn" onclick="copyFDL()">FDL</button>
<button onclick="openTemplate('firstModal')">1rst WORK</button>
<button onclick="openTemplate('cbrModal')">CBR</button>
<button onclick="openTemplate('ffiModal')">FFI</button>
<button onclick="openTemplate('payModal')">Paystubs</button>
<button onclick="openTemplate('businessModal')">Business</button>
<button onclick="openTemplate('incorpModal')">Incorp</button>
<button onclick="openTemplate('assesModal')">Asses</button>
<button onclick="openTemplate('incompleteModal')">Incomplete</button>
<button onclick="openTemplate('finalModal')">Final</button>
<button onclick="openTemplate('factorModal')">Factor</button>
<button onclick="openTemplate('gnaHighModal')">GNA high</button>
<button onclick="openTemplate('gnaFfiModal')">GNA FFI</button>
<button id="resetAllTemplatesBtn" onclick="resetAllTemplates()">Reset</button>

</section>

<!-- ================= CUSTOM BUTTONS ================= -->
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

<!-- ================= DATE CALCULATOR ================= -->
<section>
<h2>Date Calculator</h2>
<div class="date-layout">
<div>
<input id="baseDate" class="calendar" type="hidden">
</div>
<div class="date-controls">
<div>
<div id="baseInfo"></div>
<button onclick="setToday()">Today</button>
<input type="number" id="daysToAdd" placeholder="Days (-4 or 7)">
</div>
<button onclick="calculateDate()">Calculate</button>
<div>
<div>
<button onclick="quickAdd(7,this)">+7</button>
<button onclick="quickAdd(18,this)">+18</button>
<button onclick="quickAdd(31,this)">+31</button>
</div>
<div id="dateResult"></div>
</div>
</div>
</section>

<!-- ================= MAPS ================= -->
<section>
<h2>Street View</h2>
<input type="text" id="streetSearch" placeholder="Buscar dirección">
<button onclick="searchStreet()">Buscar</button>
<br><br>
<iframe
id="streetFrame"
width="100%"
height="400"
style="border:0;border-radius:12px;display:none"
loading="lazy">
</iframe>
</section>
<!-- ================= GOOGLE SEARCH ================= -->
<section>
<h2>Google Search</h2>
<input type="text" id="googleSearch" placeholder="Buscar en Google">
<button onclick="searchGoogle()">Buscar</button>
<br><br>

<iframe
id="googleFrame"
width="100%"
height="400"
style="border:0;border-radius:12px;display:none"
loading="lazy">
</iframe>
</section>
<!-- ================= CURRENCY CONVERTER (AL FINAL) ================= -->
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
</div>

<!-- ================= 1rst WORK MODAL ================= -->
<div id="firstModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeFirst()">✖</span>
    <h2>1rst WORK</h2>
   <strong>Select title : </strong><br>
<button id="tFac" onclick="setFirstTitle('Fac confirm')">Fac confirm</button>
<button id="tCancel" onclick="setFirstTitle('cancel')">cancel</button>
<button id="tNoCancel" onclick="setFirstTitle('no cancel')">no cancel</button>
<button id="tPay" onclick="setFirstTitle('pay')">pay</button>
<button id="tReturn" onclick="setFirstTitle('return')">return</button><br><br>
    1.- asdfads: <input id="f1"><br><br>
    2.- asdfads: <input id="f2"><br><br>
    3.- asdfads: <input id="f3"><br><br>
    4.- asdfads: <input id="f4"><br><br>
    5.- asdfads: <input id="f5"><br><br>
    6.- asdfads: <input id="f6">
    <div class="copy-center">
<button id="copyFirstBtn" onclick="copyFirst()">Copy FFI</button>
<button id="resetFirstBtn" onclick="resetFirst()">Reset</button>
</div>
  </div>
</div>
<!-- ================= CBR MODAL ================= -->
<div id="cbrModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('cbrModal')">✖</span>
    <h3>CBR</h3>
    <strong>Type:</strong>
    <input id="cbrType" placeholder="XXXX">
    <br><br>
    <strong>AVAIL:</strong>
    <input id="cbrAvail" placeholder="$$$$">
    <strong>CR:</strong>
    <input id="cbrCR" placeholder="$$$$">
    <strong>DC %:</strong>
    <input type="number" id="cbrDC" placeholder="##">
    <br><br>
    <strong>OPEN:</strong>
    <input type="number" id="cbrOpen" placeholder="##">
    <strong>DATE:</strong>
    <input type="number" id="cbrDate" placeholder="##">
    <br><br>
    <strong>DATE OF:</strong>
    <input type="number" id="cbrDateOf" placeholder="##">
    <br><br>
    <strong>INQUIR:</strong>
    <input type="number" id="cbrInquir" placeholder="##">
    <strong>FIC:</strong>
    <input type="number" id="cbrFic" placeholder="##">
    <br><br>
    <strong>MISC:</strong>
    <input id="cbrMisc" placeholder="XXXX">
    <strong>ON FILE:</strong>
    <input id="cbrFile" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyCBRBtn" onclick="copyCBR()">Copy</button>
      <button id="resetCBRBtn" onclick="resetCBR()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= FFI MODAL ================= -->
<div id="ffiModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('ffiModal')">✖</span>
    <h3>FFI</h3>
    <!-- DOC VERIFY -->
    <strong>DOC verify / Visual Checks</strong>
    <button id="docYes" onclick="setDocVerify('Yes')">Yes</button>
    <button id="docNo" onclick="setDocVerify('No')">No</button>
    <br><br>
    <!-- 60% PROXY -->
    <strong>60% Proxy</strong>
    <button id="proxyYes" onclick="setProxy('Yes')">Yes</button>
    <button id="proxyNo" onclick="setProxy('No')">No</button>
    <button id="proxySelfEmployee" onclick="setProxy('Self-employee')">Self-employee</button>
       <input type="number" id="percentInput" placeholder="%">
    <strong>%, Reported: $</strong>
       <input type="number" id="reportInput" placeholder="$">
    <!-- INPUTS -->
    <br><br>
    <strong>Payment show: $</strong>
      <button id="payYes" onclick="setPayment('Yes')">Yes</button>
      <button id="payNo" onclick="setPayment('No')">No</button>
    <br><br>
    <strong>Bank: </strong>
      <input type="text" id="bankInput" placeholder="Bank,">
    <br><br>
    <!-- Ending + Month1 + Month2 en la misma línea -->
    <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
    <strong>Ending: $</strong>
    <input type="text" id="showingInput" placeholder="Balance">
    <strong>Month1: $</strong>
    <input type="text" id="month1Input" placeholder="Month">
    <strong>Month2: $</strong>
    <input type="text" id="month2Input" placeholder="Month">
    </div>
    <br><br>
    <!-- Outcome en nueva línea -->
    <strong>Outcome: </strong>
    <input type="text" id="outcomeInput" placeholder="Outcome">
    <br><br>
    <!-- BUTTONS -->
    <div class="copy-center">
      <button id="copyFFIBtn" onclick="copyFFI()">Copy</button>
      <button id="resetFFIBtn" onclick="resetFFI()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= PAYSTUBS MODAL ================= -->
<div id="payModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('payModal')">✖</span>

    <h3>Paystubs</h3>

    <strong>Payslips:</strong>
    <input id="payPayslips" placeholder="XXXX">
    <br><br>
    <strong>Business:</strong>
    <input id="payBusiness" placeholder="XXXX">
    <br><br>
    <strong>Recip:</strong>
    <input id="payRecip" placeholder="XXXX">
    <br><br>
    <strong>Gross:</strong>
    <input id="payGross" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyPayBtn" onclick="copyPay()">Copy</button>
      <button id="resetPayBtn" onclick="resetPay()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= BUSINESS MODAL ================= -->
<div id="businessModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('businessModal')">✖</span>
    <h3>Business</h3>
    <strong>Date:</strong>
    <input id="busDate" placeholder="XXXX">
    <br><br>
    <strong>Business:</strong>
    <input id="busBusiness" placeholder="XXXX">
    <br><br>
    <strong>Name:</strong>
    <input id="busName" placeholder="XXXX">
    <br><br>
    <strong>Reg #:</strong>
    <input id="busReg" placeholder="XXXX">
    <br><br>
    <strong>Legal:</strong>
    <button id="legalSole" onclick="setLegal('sole proprietorship')">Sole</button>
    <button id="legalPartner" onclick="setLegal('partnership')">Partnership</button>
    <br><br>
    <strong>Business type:</strong>
    <input id="busType" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyBusBtn" onclick="copyBusiness()">Copy</button>
      <button id="resetBusBtn" onclick="resetBusiness()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= INCORP MODAL ================= -->
<div id="incorpModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('incorpModal')">✖</span>
    <h3>Incorp</h3>
    <strong>Business on:</strong>
    <input id="incBusinessOn" placeholder="XXXX">
    <br><br>
    <strong>Business name:</strong>
    <input id="incBusinessName" placeholder="XXXX">
    <br><br>
    <strong>Incorp #:</strong>
    <input id="incNumber" placeholder="XXXX">
    <br><br>
    <strong>Direc:</strong>
    <input id="incDirec" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyIncorpBtn" onclick="copyIncorp()">Copy</button>
      <button id="resetIncorpBtn" onclick="resetIncorp()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= ASSES MODAL ================= -->
<div id="assesModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('assesModal')">✖</span>
    <h3>ASSES</h3>
    <strong>Year:</strong>
    <input id="assYear" placeholder="XXXX">
    <br><br>
    <strong>Date:</strong>
    <input id="assDate" placeholder="XXXX">
    <br><br>
    <strong>Bus:</strong>
    <input id="assBus" placeholder="XXXX">
    <br><br>
    <strong>Bus #:</strong>
    <input id="assBusNum" placeholder="XXXX">
    <br><br>
    <strong>Part 1:</strong>
    <input id="assPart" placeholder="XXXX">
    <br><br>
    <strong>Result:</strong>
    <input id="assResult" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyAssBtn" onclick="copyAsses()">Copy</button>
      <button id="resetAssBtn" onclick="resetAsses()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= INCOMPLETE MODAL ================= -->
<div id="incompleteModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('incompleteModal')">✖</span>
    <h3>Incomplete</h3>
    <strong>We:</strong>
    <input id="incWe" placeholder="XXXX">
    <br><br>
    <strong>Dead:</strong>
    <input id="incDead" placeholder="XXXX">
    <br><br>
    <strong>Additional:</strong>
    <input id="incAdditional" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyIncBtn" onclick="copyIncomplete()">Copy</button>
      <button id="resetIncBtn" onclick="resetIncomplete()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= FINAL MODAL ================= -->
<div id="finalModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('finalModal')">✖</span>
    <h2>Final</h2>
<strong>Select title :</strong><br>
<button id="ftFac" onclick="setFinalTitle('Fac confirm')">Fac confirm</button>
<button id="ftCancel" onclick="setFinalTitle('cancel')">cancel</button>
<button id="ftNoCancel" onclick="setFinalTitle('no cancel')">no cancel</button>
<button id="ftPay" onclick="setFinalTitle('pay')">pay</button>
<button id="ftReturn" onclick="setFinalTitle('return')">return</button>
<br><br>
Reason:
<input id="finalReason">
<br><br>
Next:
<input id="finalNext">
<br><br>
<div class="copy-center">
<button id="copyFinalBtn" onclick="copyFinal()">Copy</button>
<button id="resetFinalBtn" onclick="resetFinal()">Reset</button>
</div>
  </div>
</div>
<!-- ================= FACTOR MODAL ================= -->
<div id="factorModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('factorModal')">✖</span>
    <h3>Factor</h3>
    <strong>SE:</strong>
    <input id="facSE" placeholder="XXXX">
    <br><br>
    <strong>Name:</strong>
    <input id="facName" placeholder="XXXX">
    <br><br>
    <strong>Lname:</strong>
    <input id="facLname" placeholder="XXXX">
    <br><br>
    <strong>Date:</strong>
    <input id="facDate" placeholder="XXXX">
    <br><br>
    <strong>Card:</strong>
    <input id="facCard" placeholder="XXXX">
    <br><br>
    <strong>CM:</strong>
    <input id="facCM" placeholder="XXXX">
    <br><br>
    <strong>Conf:</strong>
    <input id="facConf" placeholder="XXXX">
    <br><br>
    <strong>How:</strong>
    <input id="facHow" placeholder="XXXX">
    <br><br>
    <strong>Total:</strong>
    <input id="facTotal" placeholder="XXXX">
    <br><br>
    <strong>Rec:</strong>
    <input id="facRec" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyFactorBtn" onclick="copyFactor()">Copy</button>
      <button id="resetFactorBtn" onclick="resetFactor()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= GNA HIGH MODAL ================= -->
<div id="gnaHighModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('gnaHighModal')">✖</span>
    <h3>GNA High</h3>
    <strong>Ref:</strong>
    <input id="gnaRef" placeholder="XXXX">
    <br><br>
    <strong>Link:</strong>
    <input id="gnaLink" placeholder="XXXX">
    <br><br>
    <strong>Ema:</strong>
    <input id="gnaEma" placeholder="XXXX">
    <br><br>
    <strong>CBR:</strong>
    <input id="gnaCBR" placeholder="XXXX">
    <br><br>
    <strong>Doc:</strong>
    <input id="gnaDoc" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyGnaBtn" onclick="copyGnaHigh()">Copy</button>
      <button id="resetGnaBtn" onclick="resetGnaHigh()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= GNA FFI MODAL ================= -->
<div id="gnaFfiModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('gnaFfiModal')">✖</span>
    <h3>GNA FFI</h3>
    <strong>DOC:</strong>
    <input id="gnaDocFfi" placeholder="XXXX">
    <br><br>
    <strong>60%:</strong>
    <input id="gna60" placeholder="XXXX">
    <br><br>
    <strong>End:</strong>
    <input id="gnaEnd" placeholder="XXXX">
    <br><br>
    <strong>Outcome:</strong>
    <input id="gnaOutcome" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyGnaFfiBtn" onclick="copyGnaFfi()">Copy</button>
      <button id="resetGnaFfiBtn" onclick="resetGnaFfi()">Reset</button>
    </div>
  </div>
</div>
<!-- ================= GNA FFI MODAL ================= -->
<div id="gnaFfiModal" class="ffi-modal">
  <div class="ffi-content">
    <span class="close-btn" onclick="closeTemplate('gnaFfiModal')">✖</span>
    <h3>GNA FFI</h3>
    <strong>DOC:</strong>
    <input id="gnaDocFfi" placeholder="XXXX">
    <br><br>
    <strong>60%:</strong>
    <input id="gna60" placeholder="XXXX">
    <br><br>
    <strong>End:</strong>
    <input id="gnaEnd" placeholder="XXXX">
    <br><br>
    <strong>Outcome:</strong>
    <input id="gnaOutcome" placeholder="XXXX">
    <br><br>
    <div class="copy-center">
      <button id="copyGnaFfiBtn" onclick="copyGnaFfi()">Copy</button>
      <button id="resetGnaFfiBtn" onclick="resetGnaFfi()">Reset</button>
    </div>
  </div>
</div>
<!---------------- NOTE PANEL --------------------->
<div id="notePanel" class="note-panel">

<span class="note-close" onclick="closeNote()">✖</span>

<textarea id="noteText" placeholder="Write note..."></textarea>

<div class="note-buttons">
<button id="copyNoteBtn" onclick="copyNote()">Copy</button>
<button id="resetNoteBtn" onclick="resetNote()">Reset</button>
</div>

</div>   <!-- 🔴 ESTE DIV FALTABA -->

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
function toggleIC(){
    const modal = document.getElementById("icModal");
    modal.style.display="flex";
}
function closeIC(){
    document.getElementById("icModal").style.display="none";
}
document.addEventListener("click", function(e){

const icModal = document.getElementById("icModal");
const icContent = icModal.querySelector(".ffi-content");
const icButton = document.querySelector(".ic-toggle");

if(icModal.style.display !== "flex") return;

if(icContent.contains(e.target)) return;

if(icButton.contains(e.target)) return;

icModal.style.display = "none";

});
////////////////////////////////////////////////////
//// NOTE
////////////////////////////////////////////////////
const noteToggle = document.getElementById("noteToggle");
const notePanel = document.getElementById("notePanel");
noteToggle.onclick = function(){
    notePanel.style.display =
    notePanel.style.display === "block" ? "none" : "block";
};
document.addEventListener("click", function(e){
if(!notePanel.contains(e.target) && !noteToggle.contains(e.target)){
    notePanel.style.display = "none";
}
});
function copyNote(){

let text = document.getElementById("noteText").value;

navigator.clipboard.writeText(text);

copyFeedback(document.getElementById("copyNoteBtn"));

}

function resetNote(){

document.getElementById("noteText").value="";

resetFeedback(document.getElementById("resetNoteBtn"));

}
function closeNote(){
notePanel.style.display="none";
}
const noteText = document.getElementById("noteText");

noteText.addEventListener("input", function(){

this.style.height = "auto";
this.style.height = this.scrollHeight + "px";

});
////////////////////////////////////////////////////
////                CURRENCY
////////////////////////////////////////////////////
let rates = {};

async function loadRates(){
    const res = await fetch("https://api.exchangerate-api.com/v4/latest/USD");
    const data = await res.json();
    rates = data.rates;

    convert(1);
}
function convert(from){
    if(!rates.USD) return;

    let a1=parseFloat(amount1.value)||0;
    let a2=parseFloat(amount2.value)||0;

    let c1=currency1.value;
    let c2=currency2.value;

    if(from===1){
        let usd = a1 / rates[c1];
        amount2.value = (usd * rates[c2]).toFixed(2);
    }else{
        let usd = a2 / rates[c2];
        amount1.value = (usd * rates[c1]).toFixed(2);
    }
}
function swapCurrencies(){
    let temp=currency1.value;
    currency1.value=currency2.value;
    currency2.value=temp;
    convert(1);
}

loadRates();

////////////////////////////////////////////////////
////                DATE SYSTEM
////////////////////////////////////////////////////
let resultDateHighlight = null;
let baseDateGlobal = new Date();
////////////////////////////////////////////////////
////                DATE FUNCTIONS
////////////////////////////////////////////////////
function updateBaseInfo(date){
    baseDateGlobal = new Date(date);
    let month = date.toLocaleString('default',{month:'short'}).toUpperCase();
    let day = date.getDate();
    document.getElementById("baseInfo").innerText =
        "Started Date: " + month + " " + day;
}
function setToday(){
    let today = new Date();
    baseDateGlobal = new Date(today);
    // actualizar texto
    document.getElementById("baseInfo").innerText =
        "Started Date: TODAY";
    // mover calendario
    if(calendar){
        calendar.jumpToDate(today);
    }
    // limpiar input
    document.getElementById("daysToAdd").value = "";
    // limpiar resultado
    document.getElementById("dateResult").innerText = "";
}
function highlightResult(){
    document.querySelectorAll(".flatpickr-day").forEach(day=>{
        day.classList.remove("result-day");
        if(day.dateObj){
            let d = day.dateObj.getFullYear()+"-"+(day.dateObj.getMonth()+1)+"-"+day.dateObj.getDate();
            if(d === resultDateHighlight){
                day.classList.add("result-day");
            }
        }
    });
}
function changeDays(direction){
    let base = document.getElementById("baseDate").value;
    let days = parseInt(document.getElementById("daysToAdd").value);
    if(isNaN(days)) return;
    let date = base ? new Date(base) : new Date();
    date.setDate(date.getDate() + (days * direction));
    updateCalendar(date);
}
function calculateDate(){
    let days = parseInt(document.getElementById("daysToAdd").value);
    if(isNaN(days)) return;
    let date = new Date(baseDateGlobal);
    updateBaseInfo(date);
    date.setDate(date.getDate() + days);
    updateCalendar(date);
}
function quickAdd(days,btn){
    if(btn){
        btn.classList.add("quick-press");
        setTimeout(()=>btn.classList.remove("quick-press"),150);
    }
    let date = new Date(baseDateGlobal);
    updateBaseInfo(date);
    date.setDate(date.getDate() + days);
    updateCalendar(date);
}
////////////////////////////////////////////////////
////                FUNCTION CALENDAR
////////////////////////////////////////////////////
function updateCalendar(date){
    let iso = date.getFullYear()+"-"+(date.getMonth()+1)+"-"+date.getDate();
    resultDateHighlight = iso;
    // mover calendario al mes correcto
    if(calendar){
        calendar.jumpToDate(date);
    }
    setTimeout(highlightResult,50);
    // resultado MM/DD
    let month = String(date.getMonth()+1).padStart(2,'0');
    let day = String(date.getDate()).padStart(2,'0');
    document.getElementById("dateResult").innerText = `${month}/${day}`;
}
////////////////////////////////////////////////////
//// FDL QUICK COPY           (CLIPBOARD)
////////////////////////////////////////////////////
function copyFDL(){
let text=`===========FDL===========
Asdfasdfasdfasdfasdfasdfasdfasdfasd
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("fdlBtn"));
}
function copyAllCustom(){
    navigator.clipboard.writeText(customList.join(" + "));
    copyFeedback(document.getElementById("copyAllCustomBtn"));
}
////////////////////////////////////////////////////
//// 1RST WORK SYSTEM (tipo Proxy)
////////////////////////////////////////////////////
function toggleFirst(){
    const modal = document.getElementById("firstModal");

    if(modal.style.display==="flex"){
        modal.style.display="none";
    }else{
        modal.style.display="flex";
    }
}
function closeFirst(){
    document.getElementById("firstModal").style.display="none";
}
let firstTitle="";
function setFirstTitle(value){
    firstTitle=value;
    tFac.classList.remove("title-selected");
    tCancel.classList.remove("title-selected");
    tNoCancel.classList.remove("title-selected");
    tPay.classList.remove("title-selected");
    tReturn.classList.remove("title-selected");
    if(value==="Fac confirm")tFac.classList.add("title-selected");
    if(value==="cancel")tCancel.classList.add("title-selected");
    if(value==="no cancel")tNoCancel.classList.add("title-selected");
    if(value==="pay")tPay.classList.add("title-selected");
    if(value==="return")tReturn.classList.add("title-selected");
}
function copyFirst(){
let text=`===========${firstTitle}===========
1.- ${f1.value}
2.- ${f2.value}
3.- ${f3.value}
4.- ${f4.value}
5.- ${f5.value}
6.- ${f6.value}
=======================`;
navigator.clipboard.writeText(text);
}
function copyFirst(){
let text=`===========${firstTitle}===========
1.- ${f1.value}
2.- ${f2.value}
3.- ${f3.value}
4.- ${f4.value}
5.- ${f5.value}
6.- ${f6.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyFirstBtn"));
}
function resetFirst(){
firstTitle="";
["f1","f2","f3","f4","f5","f6"]
.forEach(id=>document.getElementById(id).value="");
tFac.classList.remove("title-selected");
tCancel.classList.remove("title-selected");
tNoCancel.classList.remove("title-selected");
tPay.classList.remove("title-selected");
tReturn.classList.remove("title-selected");
resetFeedback(document.getElementById("resetFirstBtn"));
}
////////////////////////////////////////////////////
//// CBR TEMPLATE
////////////////////////////////////////////////////
function copyCBR(){
let text=`===========CBR===========
Type: ${cbrType.value} *CBR ${cbrType.value}
AVAIL: $${cbrAvail.value}  *CR: $${cbrCR.value} *DC: ${cbrDC.value} %
*OPEN ${cbrOpen.value} * DATE : ${cbrDate.value}
*DATE OF : ${cbrDateOf.value}
*INQUIR: ${cbrInquir.value} *FIC: ${cbrFic.value}
*MISC: ${cbrMisc.value} ON FILE: ${cbrFile.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyCBRBtn"));
}
function resetCBR(){
[
"cbrType",
"cbrAvail",
"cbrCR",
"cbrDC",
"cbrOpen",
"cbrDate",
"cbrDateOf",
"cbrInquir",
"cbrFic",
"cbrMisc",
"cbrFile"
].forEach(id=>document.getElementById(id).value="");
resetFeedback(document.getElementById("resetCBRBtn"));
}

////////////////////////////////////////////////////
////                     FFI TEMPLATE
////////////////////////////////////////////////////
let payStatus="";
function setPayment(value){
payStatus=value;
payYes.classList.remove("proxy-green","proxy-red");
payNo.classList.remove("proxy-green","proxy-red");
if(value==="Yes") payYes.classList.add("proxy-green");
if(value==="No") payNo.classList.add("proxy-red");
}
//                🔴 QUITAR selección visual de Proxy
let selectedProxy="";
function setProxy(value){
    selectedProxy=value;
    proxyYes.classList.remove("proxy-green");
    proxyNo.classList.remove("proxy-red");
    proxySelfEmployee.classList.remove("proxy-yellow");
    if(value==="Yes")proxyYes.classList.add("proxy-green");
    if(value==="No")proxyNo.classList.add("proxy-red");
    if(value==="Self-employee") proxySelfEmployee.classList.add("proxy-yellow");
}
function copyFFI(){
let text=`===========FFI===========
Doc Verify: ${docVerify}
60% Proxy: ${selectedProxy}, CM Prox: ${percentInput.value}% , Reported: $${reportInput.value}
Payment show: ${payStatus}
Bank: ${reportInput.value}
Ending: $${showingInput.value}, Month1: $${month1Input.value}, Month2: $${month2Input.value}
Outcome: ${outcomeInput.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyFFIBtn"));
}
function resetFFI(){
selectedProxy="";
docVerify="";
payStatus="";
[
"percentInput",
"reportInput",
"bankInput",
"showingInput",
"month1Input",
"month2Input",
"outcomeInput"
].forEach(id=>document.getElementById(id).value="");
proxyYes.classList.remove("proxy-green");
proxyNo.classList.remove("proxy-red");
proxySelfEmployee.classList.remove("proxy-yellow");
docYes.classList.remove("proxy-green");
docNo.classList.remove("proxy-red");
payYes.classList.remove("proxy-green");
payNo.classList.remove("proxy-red");
resetFeedback(document.getElementById("resetFFIBtn"));
}
let docVerify="";
function setDocVerify(value){
    docVerify=value;
    docYes.classList.remove("proxy-green","proxy-red");
    docNo.classList.remove("proxy-green","proxy-red");
    if(value==="Yes") docYes.classList.add("proxy-green");
    if(value==="No") docNo.classList.add("proxy-red");
}

////////////////////////////////////////////////////
//// FFI MODAL CONTROL
////////////////////////////////////////////////////
function toggleFFI(){
    const modal = document.getElementById("ffiModal");

    if(modal.style.display==="flex"){
        modal.style.display="none";
    }else{
        modal.style.display="flex";
    }
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

////////////////////////////////////////////////////
//// PAYSTUBS TEMPLATE
////////////////////////////////////////////////////
function copyPay(){
let text=`===========Paystubs===========
*Payslips:${payPayslips.value}
*Business: ${payBusiness.value}
*Recip: ${payRecip.value}
*Gross : ${payGross.value}
=======================`;
+
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyPayBtn"));
}
function resetPay(){
[
"payPayslips",
"payBusiness",
"payRecip",
"payGross"
].forEach(id=>document.getElementById(id).value="");
resetFeedback(document.getElementById("resetPayBtn"));
}
////////////////////////////////////////////////////
//// BUSINESS TEMPLATE
////////////////////////////////////////////////////
let legalType="";
function setLegal(value){
legalType=value;
legalSole.classList.remove("proxy-green");
legalPartner.classList.remove("proxy-green");
if(value==="sole proprietorship") legalSole.classList.add("proxy-green");
if(value==="partnership") legalPartner.classList.add("proxy-green");
}
function copyBusiness(){
let text=`===========Business===========
*Date: ${busDate.value}
*Business: ${busBusiness.value}
*Name: ${busName.value}
*Reg #: ${busReg.value}
Legal : ${legalType}
Business type: ${busType.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyBusBtn"));
}
function resetBusiness(){
legalType="";
[
"busDate",
"busBusiness",
"busName",
"busReg",
"busType"
].forEach(id=>document.getElementById(id).value="");
legalSole.classList.remove("proxy-green");
legalPartner.classList.remove("proxy-green");
resetFeedback(document.getElementById("resetBusBtn"));
}
////////////////////////////////////////////////////
//// INCORP TEMPLATE
////////////////////////////////////////////////////
function copyIncorp(){
let text=`===========Incorp===========
*Business on: ${incBusinessOn.value}
*Business name: ${incBusinessName.value}
*Incorp #: ${incNumber.value}
*Direc: ${incDirec.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyIncorpBtn"));
}
function resetIncorp(){
[
"incBusinessOn",
"incBusinessName",
"incNumber",
"incDirec"
].forEach(id=>document.getElementById(id).value="");
resetFeedback(document.getElementById("resetIncorpBtn"));
}
////////////////////////////////////////////////////
//// ASSES TEMPLATE
////////////////////////////////////////////////////
function copyAsses(){
let text=`===========ASSES===========
*Year: ${assYear.value}
*Date: ${assDate.value}
*Bus: ${assBus.value}
*Bus #: ${assBusNum.value}
*Part 1: ${assPart.value}
*Result: ${assResult.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyAssBtn"));
}
function resetAsses(){
[
"assYear",
"assDate",
"assBus",
"assBusNum",
"assPart",
"assResult"
].forEach(id=>document.getElementById(id).value="");
resetFeedback(document.getElementById("resetAssBtn"));
}
////////////////////////////////////////////////////
//// INCOMPLETE TEMPLATE
////////////////////////////////////////////////////
function copyIncomplete(){
let text=`===========Incomplete===========
*We : ${incWe.value}
*Dead: ${incDead.value}
*Additional: ${incAdditional.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyIncBtn"));
}
function resetIncomplete(){
[
"incWe",
"incDead",
"incAdditional"
].forEach(id=>document.getElementById(id).value="");
resetFeedback(document.getElementById("resetIncBtn"));
}
////////////////////////////////////////////////////
//// FINAL TEMPLATE
////////////////////////////////////////////////////
let finalTitle="";
function setFinalTitle(value){
finalTitle=value;
ftFac.classList.remove("title-selected");
ftCancel.classList.remove("title-selected");
ftNoCancel.classList.remove("title-selected");
ftPay.classList.remove("title-selected");
ftReturn.classList.remove("title-selected");
if(value==="Fac confirm") ftFac.classList.add("title-selected");
if(value==="cancel") ftCancel.classList.add("title-selected");
if(value==="no cancel") ftNoCancel.classList.add("title-selected");
if(value==="pay") ftPay.classList.add("title-selected");
if(value==="return") ftReturn.classList.add("title-selected");
}
function copyFinal(){
let text=`===========${finalTitle}===========
*Reason : ${finalReason.value}
*Next : ${finalNext.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyFinalBtn"));
}
function resetFinal(){
finalTitle="";
[
"finalReason",
"finalNext"
].forEach(id=>document.getElementById(id).value="");
ftFac.classList.remove("title-selected");
ftCancel.classList.remove("title-selected");
ftNoCancel.classList.remove("title-selected");
ftPay.classList.remove("title-selected");
ftReturn.classList.remove("title-selected");
resetFeedback(document.getElementById("resetFinalBtn"));
}
////////////////////////////////////////////////////
//// FACTOR TEMPLATE
////////////////////////////////////////////////////
function copyFactor(){
let text=`===========Factor===========
*SE : ${facSE.value}
*Name: ${facName.value}
*Lname : ${facLname.value}
*Date : ${facDate.value}
*Card : ${facCard.value}
*CM : ${facCM.value}
*Conf : ${facConf.value}
*How : ${facHow.value}
*Total : ${facTotal.value}
*Rec : ${facRec.value}
=======================`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyFactorBtn"));
}
function resetFactor(){
[
"facSE",
"facName",
"facLname",
"facDate",
"facCard",
"facCM",
"facConf",
"facHow",
"facTotal",
"facRec"
].forEach(id=>document.getElementById(id).value="");
resetFeedback(document.getElementById("resetFactorBtn"));
}
////////////////////////////////////////////////////
//// GNA HIGH TEMPLATE
////////////////////////////////////////////////////
function copyGnaHigh(){
let text=`***High**
Ref : ${gnaRef.value}
Link: ${gnaLink.value}
Ema: ${gnaEma.value}
CBR: ${gnaCBR.value}
Doc: ${gnaDoc.value}
**********`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyGnaBtn"));
}
function resetGnaHigh(){
[
"gnaRef",
"gnaLink",
"gnaEma",
"gnaCBR",
"gnaDoc"
].forEach(id=>document.getElementById(id).value="");
resetFeedback(document.getElementById("resetGnaBtn"));
}
////////////////////////////////////////////////////
//// GNA FFI TEMPLATE
////////////////////////////////////////////////////
function copyGnaFfi(){
let text=`***FFI-R**
DOC: ${gnaDocFfi.value}
60%: ${gna60.value}
End: ${gnaEnd.value}
Outcome: ${gnaOutcome.value}
**********`;
navigator.clipboard.writeText(text);
copyFeedback(document.getElementById("copyGnaFfiBtn"));
}
function resetGnaFfi(){
[
"gnaDocFfi",
"gna60",
"gnaEnd",
"gnaOutcome"
].forEach(id=>document.getElementById(id).value="");
resetFeedback(document.getElementById("resetGnaFfiBtn"));
}
////////////////////////////////////////////////////
//// FUNCIONES TEMPLATE
////////////////////////////////////////////////////
let customList=[];
function createCustom(){
    let label = document.getElementById("customLabel").value;
    let text = document.getElementById("customText").value;
    if(!label || !text) return;
    let wrapper = document.createElement("div");
    wrapper.style.position = "relative";
    wrapper.style.display = "inline-block";
    wrapper.style.margin = "12px";
    //         botón principal
    let btn = document.createElement("button");
    btn.innerText = label;
    btn.onclick = function(){
        customList.push(text);
        navigator.clipboard.writeText(text);
    };
    //        botón borrar en custom button
    let trash = document.createElement("div");
    trash.innerText = "X"; // podemos poner imagen
    trash.style.position = "absolute";
    trash.style.top = "-3px"; // acercarlo al boton arriba
    trash.style.right = "-1.5px"; // acercarlo derecha
    trash.style.fontSize = "9px"; // tamaño de la x o el bote
    trash.style.cursor = "pointer";
    trash.style.opacity = "0.5";  // trasnparencia
    trash.onclick = function(){
        wrapper.remove();
    };
    wrapper.appendChild(btn);
    wrapper.appendChild(trash);
    document.getElementById("customContainer").appendChild(wrapper);
    customLabel.value = "";
    customText.value = "";
}
////////////////////////////////////////////////////
//// RESET ALL TEMPLATES
////////////////////////////////////////////////////
function resetAllTemplates(){
// limpia todos los inputs de los modales
document.querySelectorAll(".ffi-modal input").forEach(input=>{
    input.value="";
});
// limpia botones seleccionados
document.querySelectorAll(".proxy-green,.proxy-red,.proxy-yellow,.title-selected")
.forEach(btn=>{
    btn.classList.remove("proxy-green","proxy-red","proxy-yellow","title-selected");
});
// reset variables usadas en templates
icList=[];
selectedProxy="";
docVerify="";
payStatus="";
firstTitle="";
finalTitle="";
legalType="";
// limpia resultado IC
const resultIC = document.getElementById("resultIC");
if(resultIC) resultIC.innerText="";
resetFeedback(document.getElementById("resetAllTemplatesBtn"));
}






////////////////////////////////////////////////////
////                CUSTOM LIST
////////////////////////////////////////////////////
function resetCustom(){
    customList=[];
    customContainer.innerHTML="";
    resetFeedback(document.getElementById("resetCustomBtn"));
}
////////////////////////////////////////////////////
////                UI HELPERS
////////////////////////////////////////////////////
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
    document.querySelectorAll("input:not([type='date'])").forEach(input=>{
        autoResizeInput(input);
        input.addEventListener("input", function(){
            autoResizeInput(this);
        });
    });
}

////////////////////////////////////////////////////
//// calendario
////////////////////////////////////////////////////
let calendar;
window.addEventListener("DOMContentLoaded", function(){
    // texto inicial
    document.getElementById("baseInfo").innerText = "Started Date: TODAY";
    calendar = flatpickr("#baseDate", {
        inline:true,
        locale:"es",
        onMonthChange:highlightResult,
        onYearChange:highlightResult,
        onChange:function(selectedDates){
            if(selectedDates.length){
                baseDateGlobal = new Date(selectedDates[0]);
                updateBaseInfo(baseDateGlobal);
            }
        }
    });

});


////////////////////////////////////////////////////
//// maps google
////////////////////////////////////////////////////
async function searchStreet(){
let address = document.getElementById("streetSearch").value;
if(!address){
alert("Escribe una dirección");
return;
}
try{
let url = "https://nominatim.openstreetmap.org/search?format=json&limit=1&q=" + encodeURIComponent(address);
let res = await fetch(url);
let data = await res.json();
if(data.length === 0){
alert("Dirección no encontrada");
return;
}
let lat = data[0].lat;
let lon = data[0].lon;
document.getElementById("streetFrame").src =
`https://www.google.com/maps?q=&layer=c&cbll=${lat},${lon}&cbp=11,0,0,0,0&output=svembed`;
document.getElementById("streetFrame").style.display="block";
}catch(error){
alert("Error buscando la dirección");
}
}
document.getElementById("streetSearch").addEventListener("keypress", function(e){
if(e.key === "Enter"){
searchStreet();
}
});


document.getElementById("googleSearch").addEventListener("keypress", function(e){
if(e.key === "Enter"){
searchGoogle();
}
});
////////////////////////////////////////////////////
//// GOOGLE SEARCH
////////////////////////////////////////////////////
function searchGoogle(){
let query = document.getElementById("googleSearch").value;
if(!query){
alert("Escribe algo para buscar");
return;
}
window.open(
"https://www.google.com/search?q=" + encodeURIComponent(query),
"_blank"
);
}

////////////////////////////////////////////////////
////        MOVEMENT OF TEMPLATES
////////////////////////////////////////////////////
let currentTemplate = null;
function openTemplate(id){
    if(currentTemplate){
        currentTemplate.style.display = "none";
    }
    const modal = document.getElementById(id);
    modal.style.display = "flex";
    currentTemplate = modal;
}
function closeTemplate(id){
    const modal = document.getElementById(id);
    modal.style.display = "none";
    if(currentTemplate === modal){
        currentTemplate = null;
    }
}
window.addEventListener("click", function(e){

    if(!currentTemplate) return;

    const content = currentTemplate.querySelector(".ffi-content");

    // si haces click dentro del modal → no cerrar
    if(content.contains(e.target)) return;

    // si haces click en un botón que abre templates → no cerrar
    if(e.target.closest("button")) return;

    currentTemplate.style.display = "none";
    currentTemplate = null;

});
document.addEventListener("keydown", function(e){

    if(e.key === "Escape" && currentTemplate){
        currentTemplate.style.display = "none";
        currentTemplate = null;
    }

});

</script>
</body>
</html>










</pre>

</section>
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

<div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">

<button onclick="setToday()">Today</button>

<input type="date" id="baseDate">

<input type="number" id="daysToAdd" min="0" placeholder="Days">

<button onclick="calculateDate()">Calculate</button>
<button onclick="quickAdd(7)">+7</button>
<button onclick="quickAdd(18)">+18</button>
<button onclick="quickAdd(31)">+31</button>

</div>

<div id="resultDate"></div>
</section>



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
    let base = document.getElementById("baseDate").value;
    let baseDate = base ? new Date(base) : new Date();
    let days = parseInt(daysToAdd.value);
    if(isNaN(days) || days < 0) return;
    baseDate.setDate(baseDate.getDate() + days);
    resultDate.innerText = 
        (baseDate.getMonth()+1) + "/" + baseDate.getDate();
}

function setToday(){
    let today = new Date();
    let formatted = today.toISOString().split("T")[0];
    document.getElementById("baseDate").value = formatted;
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
    document.querySelectorAll("input:not([type='date'])").forEach(input=>{
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
