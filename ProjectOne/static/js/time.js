

let convertToLocaltime = (domObjectTime)=>{

}
var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
document.addEventListener("DOMContentLoaded", ()=>{
    let timeObjects = document.getElementsByClassName("timeLocal");
    for (let i = 0 ; i < timeObjects.length ; i++){
        console.log(timeObjects[i])
    }
    for (let i = 0 ; i < timeObjects.length ; i++){
        let timeConvert = new Date(timeObjects[i].innerText.trim());
        timeObjects[i].innerText=timeConvert.toLocaleDateString("en-US", options);
        // console.log(timeConvert.toLocaleDateString("en-US", options));
    }

})