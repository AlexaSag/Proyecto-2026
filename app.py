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

<script>
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
</script>

</body>
</html>
"""