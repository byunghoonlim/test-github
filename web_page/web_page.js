//let a = "사랑해"; //let: 변수
//const b = "베어유?"; //const: 상수(변경 불가)

//function func_name() {

//}

//화살표 함수 (Arrow Function)
//const func_const_name = ()=>{

//}

let here_btn = document.getElementById("here_btn");

here_btn.addEventListener("click", ()=>{
    alert("사랑해");
})
            
let btn = document.getElementById("btn");
btn.addEventListener("click", ()=>{
    alert("너랑 나는 헤어질 수 없어");
})

let pink_btn = document.getElementById("pink_btn");
let content = document.getElementById("content");

pink_btn.addEventListener("click", ()=>{
    content.style.backgroundColor="pink";
})