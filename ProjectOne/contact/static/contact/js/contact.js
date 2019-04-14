function ConvertFormToJSON(form){
    var array = jQuery(form).serializeArray();
    var json = {};
    
    jQuery.each(array, function() {
        json[this.name] = this.value || '';
    });
    
    return json;
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
let SendData =  (urlLink, data, errorCode, requestHeader)=>{ 
    return new Promise((resolve, reject)=>{
        var xhr = new XMLHttpRequest();
        var url = urlLink;

        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        if (requestHeader){
            for (let i = 0 ; i < requestHeader.length ; i++){
                xhr.setRequestHeader(requestHeader[i][0], requestHeader[i][1]);
            }
        }

        xhr.onreadystatechange = function () 
        {
            if (xhr.readyState === 4 && xhr.status === 200) 
            {
                var data = JSON.parse(xhr.responseText);
                resolve(data);

                
            }
            else if (xhr.readyState === 4 && xhr.status==errorCode){
                reject(JSON.parse(xhr.responseText));
            }
                 
        };
        var stringifyData = JSON.stringify(data);
        xhr.send(stringifyData);
    });
}

document.addEventListener('DOMContentLoaded', ()=>{
    let form = document.getElementById('contactForm')
    form.addEventListener("submit",(event)=>{
        event.preventDefault();
        console.log(getCookie('csrftoken'));
        let formDat = ConvertFormToJSON($("#contactForm"));
        let requestListheader = [];
        requestListheader.push(["X-CSRFToken", getCookie('csrftoken')]);
        console.log(formDat);
        SendData("/home/",formDat, 341,requestListheader).then(reponse=>{
            console.log(reponse);
        }).catch(error=>{
            console.log(error);
        });
    })

})