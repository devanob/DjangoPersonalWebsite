;(function($){"use strict";$('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function(){if(location.pathname.replace(/^\//,'')==this.pathname.replace(/^\//,'')&&location.hostname==this.hostname){var target=$(this.hash);target=target.length?target:$('[name='+this.hash.slice(1)+']');if(target.length){$('html, body').animate({scrollTop:(target.offset().top-30)},1000,"easeInOutExpo");return false;}}});$('.js-scroll-trigger').click(function(){$('.navbar-collapse').collapse('hide');});$('body').scrollspy({target:'#mainNav',offset:0});})(jQuery);;let convertToLocaltime=(domObjectTime)=>{}
let timeStamp=()=>{let timeObjects=document.getElementsByClassName("timeLocal");for(let i=0;i<timeObjects.length;i++){let timeConvert=new Date(timeObjects[i].innerText.trim());timeObjects[i].innerText=timeConvert.toLocaleDateString("en-US",options);}}
var options={weekday:'long',year:'numeric',month:'long',day:'numeric',hour:'numeric',minute:'numeric'};document.addEventListener("DOMContentLoaded",timeStamp);;function ConvertFormToJSON(form){var array=jQuery(form).serializeArray();var json={};jQuery.each(array,function(){json[this.name]=this.value||'';});return json;}
let removeChildren=(parent)=>{while(parent.firstChild){parent.removeChild(parent.firstChild);}}
function getCookie(name){var cookieValue=null;if(document.cookie&&document.cookie!==''){var cookies=document.cookie.split(';');for(var i=0;i<cookies.length;i++){var cookie=cookies[i].trim();if(cookie.substring(0,name.length+1)===(name+'=')){cookieValue=decodeURIComponent(cookie.substring(name.length+1));break;}}}
return cookieValue;}
var csrftoken=getCookie('csrftoken');let SendData=(urlLink,data,errorCode,requestHeader)=>{return new Promise((resolve,reject)=>{var xhr=new XMLHttpRequest();var url=urlLink;xhr.open("POST",url,true);xhr.setRequestHeader("Content-Type","application/json");if(requestHeader){for(let i=0;i<requestHeader.length;i++){xhr.setRequestHeader(requestHeader[i][0],requestHeader[i][1]);}}
xhr.onreadystatechange=function()
{if(xhr.readyState===4&&xhr.status===200)
{var data=JSON.parse(xhr.responseText);resolve(data);}
else if(xhr.readyState===4&&xhr.status==errorCode){reject(JSON.parse(xhr.responseText));}};var stringifyData=JSON.stringify(data);xhr.send(stringifyData);});}
let addError=(err)=>{let mssgError=document.getElementById("messages");removeChildren(mssgError)
mssgError.classList="";mssgError.classList.add("alert");mssgError.classList.add("alert-danger");Object.keys(err).forEach(key=>{let list=document.createElement("ul");for(let i=0;i<err[key].length;i++){let listItem=document.createElement("li");listItem.innerText=err[key][i];list.appendChild(listItem);}
mssgError.appendChild(list);});setTimeout(()=>{removeChildren(mssgError);mssgError.classList="";},8000);}
let addSuccess=(success)=>{let successBox=document.getElementById("messages");removeChildren(successBox)
successBox.classList="";successBox.classList.add("alert");successBox.classList.add("alert-success");let successMssg=document.createElement("p");successMssg.innerText="Message Sent";successBox.appendChild(successMssg);setTimeout(()=>{removeChildren(successBox);successBox.classList="";},3000);}
document.addEventListener('DOMContentLoaded',()=>{let form=document.getElementById('contactForm')
form.addEventListener("submit",(event)=>{event.preventDefault();console.log(getCookie('csrftoken'));let formDat=ConvertFormToJSON($("#contactForm"));let requestListheader=[];requestListheader.push(["X-CSRFToken",getCookie('csrftoken')]);console.log(formDat);document.getElementById("submitContact").disabled=true;setTimeout(function(){document.getElementById("submitContact").disabled=false;},2000);SendData("/contacts/contactForm/",formDat,341,requestListheader).then(reponse=>{document.getElementById("submitContact").disabled=false;document.getElementById("contactForm").reset();addSuccess(reponse);}).catch(error=>{document.getElementById("submitContact").disabled=false;addError(error);});})});let fetchHTTP=(urlLink)=>{return new Promise((resolve,reject)=>{var xhr=new XMLHttpRequest();var url=urlLink;xhr.open("GET",url,true);xhr.setRequestHeader("Content-Type","application/json");xhr.onreadystatechange=function()
{if(xhr.readyState===4&&xhr.status===200)
{var data=JSON.parse(xhr.responseText);resolve(data);}
else if(xhr.readyState===4&&xhr.status==404){reject(JSON.parse(xhr.responseText));}};xhr.send();});}
let setAttributes=(el,attrs)=>{for(var key in attrs){el.setAttribute(key,attrs[key]);}}
function truncate(input,maxlength){if(input.length>maxlength)
return input.substring(0,maxlength)+'...';else
return input;};let porjectInsert=(projectArray)=>{projectArray=projectArray.filter((element)=>{if(element.project_image!=null){return true;}})
if(projectArray.length==0){return;}
let carousel_items=projectArray.map((project,index)=>{let inner_item=document.createElement('div');if(index==0){inner_item.className="carousel-item active";}
else{inner_item.className="carousel-item";}
var img=new Image();var imageContainer=document.createElement('div');imageContainer.className="imageContainer";imageContainer.appendChild(img)
inner_item.appendChild(imageContainer);img.src=project.project_image;img.alt=project.projectName;img.className="img-fluid";let link=document.createElement('a');inner_item.appendChild(link);link.href=project.project_link;let carousel_caption=document.createElement('div');carousel_caption.className="carousel-caption";link.appendChild(carousel_caption);let title=document.createElement('h1');title.innerText=project.projectName;let description=document.createElement('p');description.innerText=truncate(project.description,100);carousel_caption.appendChild(title);carousel_caption.appendChild(description);return inner_item;})
let indicator_container=document.getElementById('carousel-indicators-id');let inner_container=document.getElementById('carousel-inner-id');carousel_items.forEach((element,index)=>{"<li data-target='#carouselHeader' data-slide-to='1'></li>"
let li=document.createElement('li');if(index==0){setAttributes(li,{"data-target":"#carouselHeader","data-slide-to":index,'class':'active'});}
else{setAttributes(li,{"data-target":"#carouselHeader","data-slide-to":index});}
indicator_container.appendChild(li);inner_container.appendChild(element);});}
document.addEventListener("DOMContentLoaded",()=>{let httpURl="/projects/api-projects/projects-count/page-count=10/"
fetchHTTP(httpURl).then((data)=>{porjectInsert(data);}).catch(error=>{console.log(error);})});var canPlay=false;var v=document.createElement('video');if(v.canPlayType&&v.canPlayType('video/mp4').replace(/no/,'')){canPlay=true;}
console.log(canPlay);document.addEventListener('DOMContentLoaded',()=>{$(function(){$('[data-toggle="tooltip"]').tooltip()})})
window.addEventListener('resize',function(event){let mediaQuery=window.matchMedia("(min-width: 1000px)");adjustSkillIcons(mediaQuery);});let iconSet=document.getElementById("skill-icon");let adjustSkillIcons=(mediaQuery)=>{if(mediaQuery.matches&&!document.getElementById("container-large-screen").contains(iconSet)){iconSet.parentElement.removeChild(iconSet);document.getElementById("container-large-screen").appendChild(iconSet);}
else if(!mediaQuery.matches&&!document.getElementById("container-smaller-screen").contains(iconSet)){iconSet.parentElement.removeChild(iconSet);document.getElementById("container-smaller-screen").appendChild(iconSet);}}