

let convertToLocaltime = (domObjectTime)=>{

}
var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
document.addEventListener("DOMContentLoaded", ()=>{
    let timeObjects = document.getElementsByClassName("timeLocal");
    console.log(timeObjects);
    for (let i = 0 ; i < timeObjects.length ; i++){
        let timeConvert = new Date(timeObjects[i].innerText);
        timeObjects[i].innerText=timeConvert.toString()
        console.log(timeConvert.toLocaleDateString("en-US", options));
    }

})