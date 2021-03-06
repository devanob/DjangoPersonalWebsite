function ConvertFormToJSON(form){
    var array = jQuery(form).serializeArray();
    var json = {};
    
    jQuery.each(array, function() {
        json[this.name] = this.value || '';
    });
    
    return json;
}
/**
 * 
 * @param {*} parent - Parent node- all of which children are to be removed
 */
let removeChildren = (parent) =>{
    while (parent.firstChild) {
    parent.removeChild(parent.firstChild);
    }
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
let addError = (err)=>{
    let mssgError = document.getElementById("messages");
    removeChildren(mssgError)
    mssgError.classList = "";
    mssgError.classList.add("alert");
    mssgError.classList.add("alert-danger");
    Object.keys(err).forEach(key=>{
       let list = document.createElement("ul");
       for (let i = 0 ; i < err[key].length; i++){
            let listItem = document.createElement("li");
            listItem.innerText = err[key][i];
            list.appendChild(listItem);
       }
       mssgError.appendChild(list);
    });
    setTimeout(
        ()=>{
            removeChildren(mssgError);
            mssgError.classList = "";
        }, 8000);

}

let addSuccess = (success)=>{
    let successBox = document.getElementById("messages");
    removeChildren(successBox)
    successBox.classList = "";
    successBox.classList.add("alert");
    successBox.classList.add("alert-success");
    let successMssg = document.createElement("p");
    successMssg.innerText = "Message Sent";
    successBox.appendChild(successMssg);
    setTimeout(
        ()=>{
            removeChildren(successBox);
            successBox.classList = "";
        }, 3000);

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
        document.getElementById("submitContact").disabled = true;
        setTimeout(
            function(){
               document.getElementById("submitContact").disabled = false;
            }, 2000);
        SendData("/contacts/contactForm/",formDat, 341,requestListheader).then(reponse=>{
            document.getElementById("submitContact").disabled = false;
            document.getElementById("contactForm").reset();
            addSuccess(reponse);

        }).catch(error=>{
            document.getElementById("submitContact").disabled = false;
            addError(error);
        });
    })

})