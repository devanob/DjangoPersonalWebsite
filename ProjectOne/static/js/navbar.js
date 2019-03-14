let viewableItem= (element) =>{

        let elemTop = element.offsetTop;
        let elemBottom = elemTop + element.offsetHeight;
        let viewportTop = window.scrollY;
        let viewportBottom = viewportTop + window.innerHeight;
        // console.log("elementBotton: "+elemBottom);
        // console.log("viewPortTop: "+viewportTop);
        // console.log("viewPortBottom: "+viewportBottom);
        // console.log("elementtop: "+elemTop);
        return elemBottom >= viewportTop;
}
let headerViewableBefore = true;// True By Default
let scrollEventHandlier = () =>{
    let header = document.getElementById("headerSection");
    //console.log(window.scrollY);
    //console.log("Scrool Event Working");
    let headerViewable = viewableItem(header);
    if (headerViewable && headerViewableBefore == false){ //We'll Need To Chnage Styling
        headerViewableBefore = true;
        let navibar  = document.getElementById("navbarTop");
        navibar.classList.add("navbar-custom");
        navibar.classList.remove("navbar-dark");
        navibar.classList.remove("bg-dark");

        console.log("In Veiw Port Again");
    }
    else if (!headerViewable && headerViewableBefore == true){ //We'll Need To chnage styling back
        headerViewableBefore = false;
        let navibar  = document.getElementById("navbarTop");
        navibar.classList.add("navbar-dark");
        navibar.classList.add("bg-dark");
        navibar.classList.remove("navbar-custom");
        console.log("Not In View Port Again");
    }
}
document.addEventListener("scroll",scrollEventHandlier);

document.addEventListener("DOMContentLoaded", () =>{
    let header = document.getElementById("headerSection");
    let isViewablle = viewableItem(header);
    if (!isViewablle){
        let navibar  = document.getElementById("navbarTop");
        let headerViewableBefore = false;
        navibar.classList.add("navbar-dark");
        navibar.classList.add("bg-dark");
        navibar.classList.remove("navbar-custom");
    }
;
});


