<script>

/* ========================= */
/* 🚀 INIT APP */
/* ========================= */

function initApp(){
    initDarkMode();
    initIC();
    initCurrency();
    initDate();
    initFFI();
    initCustom();
}

document.addEventListener("DOMContentLoaded", initApp);


/* ========================= */
/* 🌙 DARK MODE */
/* ========================= */

function initDarkMode(){

    const darkBtn = document.querySelector(".dark-toggle");

    function updateDarkButton(){
        if(document.body.classList.contains("dark")){
            darkBtn.innerHTML = "🌞 Light";
        }else{
            darkBtn.innerHTML = "🌙 Dark";
        }
    }

    window.toggleDark=function(){
        document.body.classList.toggle("dark");
        updateDarkButton();
    }

    updateDarkButton();
}


/* ========================= */
/* 🔹 IC MODULE */
/* ========================= */

function initIC(){

    let icList=[];

    function updateIC(){
        if(icList.length===0){
            document.getElementById("resultIC").innerText="";
            return;
        }
        document.getElementById("resultIC").innerText=
        "VID: "+icList.map(x=>x+" OK").join(" + ");
    }

    window.addIC=function(v){ icList.push(v); updateIC(); }
    window.eraseIC=function(){ icList.pop(); updateIC(); }
    window.resetIC=function(){ icList=[]; updateIC(); }

    window.copyIC=function(){
        let btn=document.getElementById("copyICBtn");
        navigator.clipboard.writeText(
            document.getElementById("resultIC").innerText
        )
        .then(()=>{
            btn.classList.add("success");
            setTimeout(()=>btn.classList.remove("success"),800);
        })
        .catch(()=>{
            btn.classList.add("error");
            setTimeout(()=>btn.classList.remove("error"),800);
        });
    }
}


/* ========================= */
/* 💱 CURRENCY MODULE */
/* ========================= */

function initCurrency(){

    const rates={USD:1,MXN:17,CAD:1.35};

    window.convert=function(from){
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

    window.swapCurrencies=function(){
        let temp=currency1.value;
        currency1.value=currency2.value;
        currency2.value=temp;
        convert(1);
    }

    convert(1);
}


/* ========================= */
/* 📅 DATE MODULE */
/* ========================= */

function initDate(){

    window.calculateDate=function(){
        let days=parseInt(daysToAdd.value);
        if(isNaN(days)||days<0)return;

        let today=new Date();
        today.setDate(today.getDate()+days);

        resultDate.innerText=
        (today.getMonth()+1)+"/"+today.getDate();
    }

    window.quickAdd=function(days){
        daysToAdd.value=days;
        calculateDate();
    }
}


/* ========================= */
/* 🏢 FFI MODULE */
/* ========================= */

function initFFI(){

    let selectedProxy="";

    window.setProxy=function(value){

        selectedProxy=value;

        ["proxyYes","proxyNo","proxyNA"].forEach(id=>
            document.getElementById(id)
            .classList.remove("proxy-green","proxy-red","proxy-yellow")
        );

        if(value==="Yes")proxyYes.classList.add("proxy-green");
        if(value==="No")proxyNo.classList.add("proxy-red");
        if(value==="NA")proxyNA.classList.add("proxy-yellow");
    }

    window.copyFFI=function(){

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

    window.resetFFI=function(){

        selectedProxy="";

        ["docInput","docsInput","incomeInput","percentInput",
        "reportInput","showingInput","balanceInput","outcomeInput"]
        .forEach(id=>document.getElementById(id).value="");

        ["proxyYes","proxyNo","proxyNA"].forEach(id=>
            document.getElementById(id)
            .classList.remove("proxy-green","proxy-red","proxy-yellow")
        );
    }
}


/* ========================= */
/* ⚙️ CUSTOM MODULE */
/* ========================= */

function initCustom(){

    let customList=[];

    window.createCustom=function(){

        let label=customLabel.value;
        let text=customText.value;

        if(!label||!text)return;

        let btn=document.createElement("button");
        btn.className="custom-btn";
        btn.innerText=label;

        btn.onclick=function(){
            customList.push(text);
            navigator.clipboard.writeText(text);
        };

        customContainer.appendChild(btn);

        customLabel.value="";
        customText.value="";
    }

    window.copyAllCustom=function(){
        navigator.clipboard.writeText(customList.join(" + "));
    }

    window.resetCustom=function(){
        customList=[];
        customContainer.innerHTML="";
    }
}

</script>