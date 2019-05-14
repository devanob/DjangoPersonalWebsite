var canPlay = false;
var v = document.createElement('video');
if(v.canPlayType && v.canPlayType('video/mp4').replace(/no/, '')) {
    canPlay = true;
}

console.log(canPlay);


document.addEventListener('DOMContentLoaded', () =>{
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    
    })

  })