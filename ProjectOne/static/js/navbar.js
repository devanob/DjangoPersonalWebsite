
let viewableItem= (element) =>{

        let elemTop = element.offsetTop;
        let elemBottom = elemTop + element.offsetHeight;
        let viewportTop = window.scrollY;
        let viewportBottom = viewportTop + window.innerHeight;
        return elemBottom <= viewportBottom && elemTop >= viewportTop ;
}
let headerViewableBefore = true;// True By Default
let helperScrollEventHandlier = (element)=>{
    let headerViewable = viewableItem(element);
    if (headerViewable && headerViewableBefore == false){ //We'll Need To Chnage Styling
        headerViewableBefore = true;
        let navibar  = document.getElementById("navbarTop");
        navibar.classList.add("navbar-custom");
        navibar.classList.remove("navbar-dark-custom", "solid");
        return false;
    }
    else if (!headerViewable && headerViewableBefore == true){ //We'll Need To chnage styling back
        headerViewableBefore = false;
        let navibar  = document.getElementById("navbarTop");
        navibar.classList.add("navbar-dark-custom", "solid");
        navibar.classList.remove("navbar-custom");
        return true;
    }
    
    
}
let scrollEventHandlier = () =>{
    let viewAbles = document.getElementsByClassName("viewables");
    for (let i = 0 ; i < viewAbles.length; i++){
      if (helperScrollEventHandlier(viewAbles[i])){
        return;
      }
    }
    hideNavScroll();
}
document.addEventListener("scroll",scrollEventHandlier);

let setViewAvaibility = (element)=>{
    let isViewable = viewableItem(element);
    if (!isViewable){
        let navibar  = document.getElementById("navbarTop");
        navibar.classList.add("navbar-dark-custom", "solid");
        navibar.classList.remove("navbar-custom");
        return false;
    }
    return true;
}

let loadNav = ()=>{
    let allViewable = document.getElementsByClassName("viewables");
    console.log(allViewable);
    for (let i = 0 ; i < allViewable.length; i++){
      if(setViewAvaibility(allViewable[i])){
        return; // if any viewable item is in the view port then return 
      }
    }
    let navibar  = document.getElementById("navbarTop");
    navibar.classList.add("navbar-dark-custom", "solid");
    navibar.classList.remove("navbar-custom");
    


}

if(document.readyState === 'loading'){

  document.addEventListener('DOMContentLoaded',loadNav );

}
else{

  loadNav()
}
//Nav Bar Interaction 
var prevScrollpos = window.pageYOffset;
let hideNavScroll =()=>{
  var currentScrollPos = window.pageYOffset;
  let navibar  = document.getElementById("navbarTop");
  if (navibar.classList.contains('navbar-dark-custom')){
    if (prevScrollpos > currentScrollPos) {
      
      navibar.classList.add("solid");
      navibar.classList.remove("light");
      
    } else {
      navibar.classList.add("light");
      navibar.classList.remove("solid");
      
    }
  }
  prevScrollpos = currentScrollPos;
}

