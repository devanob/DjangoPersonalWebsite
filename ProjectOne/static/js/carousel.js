//fetch data from an api using get
let fetchHTTP =  (urlLink)=>{ 
    return new Promise((resolve, reject)=>{
        var xhr = new XMLHttpRequest();
        var url = urlLink;

        xhr.open("GET", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function () 
        {
            if (xhr.readyState === 4 && xhr.status === 200) 
            {
                var data = JSON.parse(xhr.responseText);
                resolve(data);

                
            }
            else if (xhr.readyState === 4 && xhr.status == 404){
                reject(JSON.parse(xhr.responseText));
            }
                 
        };
      xhr.send();
    });
}

let  setAttributes =(el, attrs) => {
    for(var key in attrs) {
      el.setAttribute(key, attrs[key]);
    }
  }

function truncate(input, maxlength) {
    if (input.length > maxlength)
       return input.substring(0,maxlength) + '...';
    else
       return input;
 };
//inserts each project to html element to be added to the homepage
let porjectInsert =(projectArray) =>{
    console.log(projectArray);
    projectArray = projectArray.results.filter((element)=>{
        if (element.project_image != null){
            return true;
        }
    })
    if (projectArray.length == 0){
        return;
    }
    let carousel_items= projectArray.map( (project,index) =>{
        //map all api-request to div to be displayed in the hompage carousel 
        let inner_item = document.createElement('div');
        if (index == 0){
            inner_item.className="carousel-item active";
        }
        else {
            inner_item.className="carousel-item";
        }
        //img main slide 
        var img = new Image();
        var imageContainer = document.createElement('div');
        imageContainer.className="imageContainer";
        imageContainer.appendChild(img)
        inner_item.appendChild(imageContainer);
        img.src=project.project_image;
        img.alt=project.projectName;
        img.className="img-fluid";
        //project-img-end
        //create clickable link and item_text
        let link= document.createElement('a');
        inner_item.appendChild(link);
        link.href= project.project_link;
        let carousel_caption = document.createElement('div');
        carousel_caption.className = "carousel-caption";
        link.appendChild(carousel_caption);
        //Title 
        let title= document.createElement('h1');
        title.innerText = project.projectName;
        //Description
        let description = document.createElement('p');
        description.innerText = truncate(project.description,100);
        carousel_caption.appendChild(title);
        carousel_caption.appendChild(description);
        return inner_item;

 
    })
    //Add indicator To items 
    let indicator_container = document.getElementById('carousel-indicators-id');
    let inner_container = document.getElementById('carousel-inner-id');
    carousel_items.forEach((element,index) => {
        "<li data-target='#carouselHeader' data-slide-to='1'></li>"
        let li = document.createElement('li');
        if (index == 0 ){
            setAttributes(li, { "data-target":"#carouselHeader","data-slide-to":index , 'class': 'active'});
        }
        else {
            setAttributes(li, { "data-target":"#carouselHeader","data-slide-to":index });
        }
        indicator_container.appendChild(li);
        inner_container.appendChild(element);
        
    });
}
document.addEventListener("DOMContentLoaded", ()=>{

    let httpURl = "/projects/api-projects/projects/?page_size=10"
    fetchHTTP(httpURl).then((data)=>{
        porjectInsert(data);
    }).catch(error=>{
        console.log(error);
    })
})

console.log("Testing Compression3");
